# Linux OS: Power Management

**Status:** Draft
**Version:** v1.0.0
**Last Updated:** 2026-04-04

## Overview

The CM5 (Raspberry Pi Compute Module 5) must respond to two hardware power events:
1. **LTC3350 BACKUP trigger** — early warning that mains power has failed and the supercap hold-up has begun (~310mV above the PWR_GD trip point, ~14.5 seconds of hold-up available)
2. **PWR_GD LOW** — last-resort signal from MCP121T-450E voltage supervisor when 5V_MAIN falls below 4.5V

The recommended approach is **Option C**: poll the LTC3350 via I²C for the BACKUP alert as the primary early-warning mechanism, with the PWR_GD GPIO as a hard backstop interrupt. This gives the CM5 the full 14.5-second hold-up window to perform a graceful shutdown.

## Hardware Signals

| Signal | GPIO | Pull-up | Source | Trigger |
|---|---|---|---|---|
| PWR_GD | TBD (see Controller/Design_Spec.md) | R3 10kΩ to 3V3_ENIG (Controller board) | MCP121T-450E U8 | Active LOW: 5V_MAIN < 4.5V |
| LTC3350 ALERT | I²C (0x09 address) | R7/R8 4.7kΩ on SDA/SCL | LTC3350 U3 | BACKUP bit set when 5V_MAIN < 4.81V |

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
# PWR_GD emergency shutdown backstop (MCP121T-450E, active-low)
dtoverlay=gpio-shutdown,gpio_pin=<TBD>,active_low=1,gpio_pull=up
```

Replace `<TBD>` with the actual CM5 GPIO number assigned to PWR_GD (see `Controller/Design_Spec.md` GPIO mapping table). The `gpio_pull=up` parameter enables the CM5 internal weak pull-up as a secondary pull-up alongside the external R3 (10kΩ).

The `gpio-shutdown` overlay triggers `systemctl poweroff` on a falling edge of the specified GPIO. With the external R3 and MCP121T open-drain output, the signal is normally HIGH (5V_MAIN stable) and goes LOW only when 5V_MAIN drops below 4.5V.

#### Alternative: Manual device tree node

For more control (e.g., custom pre-shutdown actions), use a gpio-keys node instead:

```dts
/ {
    enigma_pwr_fail: enigma-pwr-fail {
        compatible = "gpio-keys";
        pwr-good {
            label = "PWR_GD";
            gpios = <&gpio <TBD> GPIO_ACTIVE_LOW>;
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
|---|---|---|
| 5V_MAIN < 4.81V | ~0ms | LTC3350 BACKUP asserted; I²C daemon detects within 500ms |
| Daemon initiates `systemctl poweroff` | ~500ms | OS begins graceful shutdown |
| OS syncs filesystems, halts | ~10–15s | ROTOR_EN de-asserted; CM5 PMIC halted |
| 5V_MAIN < 4.50V | ~14.5s | MCP121T fires; PWR_GD LOW (backstop, already halted) |
| 5V_MAIN → 0V | ~15–16s | Supercap fully depleted |

## Dependencies

- Python package: `smbus2` (`pip3 install smbus2`)
- Python package: `systemd` (`pip3 install systemd-python`) for sd_notify
- I²C enabled on CM5 (`dtparam=i2c_arm=on` in config.txt)
- `enigma-power-monitor.service` installed and enabled (`systemctl enable enigma-power-monitor`)

## Open Items

- [ ] Confirm CM5 GPIO pin number for PWR_GD (update `<TBD>` above once GPIO mapping is finalised in Controller/Design_Spec.md)
- [ ] Verify LTC3350 I²C address (0x09 is default; may change based on ADDR pin strapping — check schematic)
- [ ] Test hold-up timing under actual CM5 load profile (5W assumed; measure at first prototype)
- [ ] Consider adding LTC3350 charge status polling (SOC readout) for optional status LED control from software
