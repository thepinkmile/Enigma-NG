# Controller Board Layout Visualisations

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-25

---

## 1. Rear Dock Interfaces

The Controller is the fixed motherboard of the enclosure and carries both removable-board docks:

- **J1 / J2 / J3** — three TE 10-position connectors to the Power Module
- **J4 / J5** — two Molex EXTreme Guardian HD hybrid connectors to the Stator

```text
rear edge of Controller

 [ J4 ] [ J5 ]   [ J1 ] [ J2 ] [ J3 ]
  to Stator          to Power Module
```

---

## 2. Controller ↔ Power Module Dock

### 2.1 J1 — Main Regulated Rails

| Allocation | Notes |
| :--- | :--- |
| `3 × 5V_MAIN` | Primary regulated 5V feed from PM to Controller |
| `2 × 3V3_ENIG` | Clean logic rail feed from PM to Controller |
| `5 × GND` | Shared return path |

**Connector family:** TE `1-1674231-1` (Controller receptacle) ↔ `1123684-7` (PM plug), 10 positions,
2.5 mm pitch, 6 A/contact.

**Reference datasheets:** [`TE-1-1674231-1-datasheet.md`](../../Datasheets/TE-1-1674231-1-datasheet.md),
[`TE-1123684-7-datasheet.md`](../../Datasheets/TE-1123684-7-datasheet.md)

### 2.2 J2 — PoE Auxiliary Feed

| Allocation | Notes |
| :--- | :--- |
| `3 × VIN_POE_12V` | Regulated PoE-derived 12V-class auxiliary feed from Controller PoE front-end into PM OR-ing stage |
| `7 × GND` | Shared return path |

### 2.3 J3 — Low-Speed Control / Telemetry

| Signal | Direction | Notes |
| :--- | :--- | :--- |
| `I2C_SDA` | Bidir | Shared PM telemetry and PM-local GPIO-expander bus |
| `I2C_SCL` | Bidir | Shared PM telemetry and PM-local GPIO-expander bus |
| `PM_IO_INT_N` | PM -> CTRL | Active-low interrupt from PM `PCA9534APWR` |
| `PWR_GD` | PM -> CTRL | Direct rail-health telemetry from MCP121T |
| `ROTOR_EN_N` | CTRL -> PM | Direct 3V3_ENIG LDO enable control |
| `PWR_BUT` | PM -> CTRL | Direct CM5 PMIC power-button path |
| `LED_PWR_N` | CTRL -> PM | Direct CM5 power-state indication for the SW2 hardware LED logic |
| `3 × GND` | — | Guards / return path |

---

## 3. Controller ↔ Stator Dock

### 3.1 J4 — 5V_MAIN-Biased Hybrid Dock

| Contact group | Allocation |
| :--- | :--- |
| Power blades | `4 × 5V_MAIN`, `1 × GND` |
| Signal field | additional `GND` guards / returns |

### 3.2 J5 — 3V3_ENIG + JTAG / I2C Hybrid Dock

| Contact group | Allocation |
| :--- | :--- |
| Power blades | `4 × 3V3_ENIG`, `1 × GND` |
| Signal field | guarded `TCK`, `TMS`, `TDI`, `TTD_RETURN`, `I2C1_SDA`, `I2C1_SCL`, remaining signal contacts = `GND` |

**Connector family:** Molex `2195630015` receptacle on Controller ↔ `2195620015` plug on Stator.

**Reference datasheets:** [`Molex-2195630015-datasheet.md`](../../Datasheets/Molex-2195630015-datasheet.md),
[`Molex-2195630015-drawings.md`](../../Datasheets/Molex-2195630015-drawings.md),
[`Molex-2195620015-datasheet.md`](../../Datasheets/Molex-2195620015-datasheet.md),
[`Molex-2195620015-drawings.md`](../../Datasheets/Molex-2195620015-drawings.md),
[`Molex-ExtremeGuardianHD-2141130000-PS-000-specification.md`](../../Datasheets/Molex-ExtremeGuardianHD-2141130000-PS-000-specification.md)

The `J5` logic connector deliberately groups the JTAG cluster and `TTD_RETURN` with the `3V3_ENIG`
feed. The `J4` connector is reserved for 5V delivery and return-current support.

---

## 4. External I/O Placement

```text
right edge of Controller

 [ RJ45 + PoE front-end ]
 [ USB 3.0 stacked Type-A ]
 [ HDMI ]
```

- The Controller owns the **RJ45, Ethernet ESD, magnetics, and PoE PD / ACF front-end**.
  The PoE front-end passes its regulated auxiliary feed into the Power Module over `J2`.
- `J9` and `J10` are internal-only connectors and are not part of the external I/O edge.
  `J9` sits between `J5` and the Power Module mounting area so it can route by ribbon cable into
  the future in-lid touchscreen assembly, while `J10` serves the CM5 active-cooler heatsink fan.

---

## 5. Placement Summary

```text
rear / dock edge
 ________________________________________________________________________
|     [J4] [J5]             [J9]               | (Power Module mounting) |
|                          _________________   | [J1]               [J3] |
|  [ JDB headers ]        |                 |  |          [J2]           |
|                         |      CM5        |  |_________________________|
|                         |     Module      |                            |
|                         | [ Low-Profile ] |                     [RJ45] |
|                         | [    Area     ] |                     [USB3] |
| [ ACTUATION MODULE ]    |_________________|                     [HDMI] |
|________________________________________________________________________|
left side / internal                                            right side
```

The Controller is the only board that must be inserted as the enclosure reference part.
The Power Module and Stator then dock into it as mechanically independent service modules.

For the shared **Actuation Module**, the Controller shall reserve the mounted-module shadow as a
**no-component placement zone** except for the two Samtec host sockets and the copper / vias needed to
route them. This preserves the daughterboard clearance set by the Samtec stack, keeps the manual-fit
loom / service headers accessible on the outward face of the inverted AM, and avoids creating a
thermally enclosed pocket around the local controller.
