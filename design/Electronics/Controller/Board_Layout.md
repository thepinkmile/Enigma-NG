# Controller Board Layout Visualisations

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-19

---

## 1. Rear Dock Interfaces

The Controller is now the fixed motherboard of the enclosure and carries both removable-board docks:

- **J1A / J1B / J1C** — three TE 10-position connectors to the Power Module
- **J2A / J2B** — two Molex EXTreme Guardian HD hybrid connectors to the Stator

```text
rear edge of Controller

 [ J2A ] [ J2B ]   [ J1A ] [ J1B ] [ J1C ]
  to Stator          to Power Module
```

---

## 2. Controller ↔ Power Module Dock

### J1A — Main Regulated Rails

| Allocation | Notes |
| :--- | :--- |
| `3 × 5V_MAIN` | Primary regulated 5V feed from PM to Controller |
| `2 × 3V3_ENIG` | Clean logic rail feed from PM to Controller |
| `5 × GND` | Shared return path |

**Connector family:** TE `1-1674231-1` (Controller receptacle) ↔ `1123684-7` (PM plug), 10 positions,
2.5 mm pitch, 6 A/contact.

**Reference PDFs:** [`TE-1-1674231-1-datasheet.pdf`](../../Datasheets/TE-1-1674231-1-datasheet.pdf),
[`TE-1123684-7-datasheet.pdf`](../../Datasheets/TE-1123684-7-datasheet.pdf)

### J1B — PoE Auxiliary Feed

| Allocation | Notes |
| :--- | :--- |
| `3 × VIN_POE_12V` | Regulated PoE-derived 12V-class auxiliary feed from Controller PoE front-end into PM OR-ing stage |
| `7 × GND` | Shared return path |

### J1C — Low-Speed Control / Telemetry

| Signal | Direction | Notes |
| :--- | :--- | :--- |
| `I2C1_SDA` | Bidir | Shared PM telemetry and PM-local GPIO-expander bus |
| `I2C1_SCL` | Bidir | Shared PM telemetry and PM-local GPIO-expander bus |
| `PM_IO_INT_N` | PM -> CTRL | Active-low interrupt from PM `PCA9534APWR` |
| `PWR_GD` | PM -> CTRL | Direct rail-health telemetry from MCP121T |
| `ROTOR_EN` | CTRL -> PM | Direct 3V3_ENIG LDO enable control |
| `PWR_BUT` | PM -> CTRL | Direct CM5 PMIC power-button path |
| `4 × GND` | — | Guards / return path |

---

## 3. Controller ↔ Stator Dock

### J2A — 5V_MAIN-Biased Hybrid Dock

| Contact group | Allocation |
| :--- | :--- |
| Power blades | `4 × 5V_MAIN`, `1 × GND` |
| Signal field | additional `GND` guards / returns |

### J2B — 3V3_ENIG + JTAG / I2C Hybrid Dock

| Contact group | Allocation |
| :--- | :--- |
| Power blades | `4 × 3V3_ENIG`, `1 × GND` |
| Signal field | guarded `TCK`, `TMS`, `TDI`, `TTD_RETURN`, `I2C1_SDA`, `I2C1_SCL`, remaining signal contacts = `GND` |

**Connector family:** Molex `2195630015` receptacle on Controller ↔ `2195620015` plug on Stator.

**Reference PDFs:** [`Molex-2195630015-datasheet.pdf`](../../Datasheets/Molex-2195630015-datasheet.pdf),
[`Molex-2195630015-drawings.pdf`](../../Datasheets/Molex-2195630015-drawings.pdf),
[`Molex-2195620015-datasheet.pdf`](../../Datasheets/Molex-2195620015-datasheet.pdf),
[`Molex-2195620015-drawings.pdf`](../../Datasheets/Molex-2195620015-drawings.pdf),
[`Molex-ExtremeGuardianHD-2141130000-PS-000-specification.pdf`](../../Datasheets/Molex-ExtremeGuardianHD-2141130000-PS-000-specification.pdf)

The `J2B` logic connector deliberately groups the JTAG cluster and `TTD_RETURN` with the `3V3_ENIG`
feed. The `J2A` connector is reserved for 5V delivery and return-current support.

---

## 4. External I/O Placement

```text
top / right edge of Controller

 [ RJ45 + PoE front-end ]
 [ USB 3.0 stacked Type-A ]
 [ HDMI ]
 [ optional DSI1 / fan header ]
```

- The Controller owns the **RJ45, Ethernet ESD, magnetics, and PoE PD / ACF front-end**.
- The Power Module no longer carries RJ45, Ethernet LED return lines, or GbE MDI routing.
- USB-C power input remains local to the Power Module.

---

## 5. Diagnostic Banks

### Diagnostic Bank-Alpha — Power Module Dock

| Pin | Signal | Description |
| :--- | :--- | :--- |
| 1 | `5V_MAIN_A` | J1A regulated 5V feed sample |
| 2 | `5V_MAIN_B` | J1A regulated 5V feed sample |
| 3 | `3V3_ENIG_A` | J1A logic-rail sample |
| 4 | `3V3_ENIG_B` | J1A logic-rail sample |
| 5 | `VIN_POE_12V` | J1B PoE auxiliary feed sample |
| 6 | `I2C1_SDA` | PM telemetry bus |
| 7 | `I2C1_SCL` | PM telemetry bus |
| 8 | `PM_IO_INT_N` | PM expander interrupt |
| 9 | `PWR_GD` | Direct PM rail-health signal |
| 10 | `ROTOR_EN` | Direct PM LDO enable |
| 11 | `PWR_BUT` | CM5 PMIC power-button path |
| 12 | `GND` | Signal ground |
| 13 | `GND` | Signal ground |
| 14 | `GND` | Signal ground |
| 15 | Spare | Reserved |
| 16 | Spare | Reserved |
| 17 | Spare | Reserved |
| 18 | Spare | Reserved |
| 19 | `GND_CHASSIS` | Controller local shield/chassis reference only |
| 20 | `GND` | System ground |

### Diagnostic Bank-Beta — Stator Dock

| Pin | Signal | Description |
| :--- | :--- | :--- |
| 1 | `5V_MAIN_J2A_1` | J2A 5V blade sample |
| 2 | `5V_MAIN_J2A_2` | J2A 5V blade sample |
| 3 | `3V3_ENIG_J2B_1` | J2B 3V3 blade sample |
| 4 | `3V3_ENIG_J2B_2` | J2B 3V3 blade sample |
| 5 | `I2C1_SDA` | Shared Stator / Settings bus |
| 6 | `I2C1_SCL` | Shared Stator / Settings bus |
| 7 | `TCK` | JTAG clock |
| 8 | `TMS` | JTAG mode |
| 9 | `TDI` | JTAG data in |
| 10 | `TTD_RETURN` | JTAG return from Reflector chain |
| 11 | `GND` | Logic guard |
| 12 | `GND` | Logic guard |
| 13 | `GND` | Power return |
| 14 | `GND` | Power return |
| 15 | Spare | Reserved |
| 16 | Spare | Reserved |
| 17 | Spare | Reserved |
| 18 | Spare | Reserved |
| 19 | `GND_CHASSIS` | Local shield/chassis reference only |
| 20 | `GND` | System ground |

---

## 6. Placement Summary

```text
 rear docks                              controller core                         user I/O
 __________________________________________________________________________________________
| [J2A][J2B] [J1A][J1B][J1C] | [ CM5 sockets + JDB headers ] | [RJ45] [USB3] [HDMI] [DSI] |
|____________________________|________________________________|_____________________________|
```

The Controller remains the only board that must be inserted as the enclosure reference part. The
Power Module and Stator then dock into it as mechanically independent service modules.
