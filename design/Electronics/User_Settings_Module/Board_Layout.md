# User Settings Module V1.0 Layout & Pinout

**Status:** In Review
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-09-21

---

## 1. Board Overview

The User Settings Module connects to the Cypher Board (top edge), Cypher-Plugboard (bottom edge),
and whichever Cypher-Input/Cypher-Output boards are installed (left edge, two connectors). No
panel-mount switches or harness connections remain on this board - the physical mounting/enclosure
location is deferred to `.copilot/todos/usm-3-part-hid-module-mechanical-review.md`.

- `U1` (I2C colour-value store, exact device TBD) holds four CM5-written RGB colour styles and
  drives their signals identically onto both HID-facing connectors (`J3`/`J4`).
- `RV1` is the shared brightness dial for the whole HID assembly.
- `BZ1` (exact device TBD) is a reserved CM5-triggered audio-warning output.
- `R1`-`R3` locally terminate the broadcast JTAG signals (`TCK`/`TMS`/`CPLD_RESET_N`).

```text
  J1 (top, mates Cypher)

  J3 (left-upper, mates       [ U1 colour store ]      J4 (left-lower, mates
   whichever HID board        [ RV1 brightness  ]        whichever HID board
   is topmost)                [ BZ1 audio (TBD) ]        is bottommost)
                               [ R1-R3 JTAG term ]

  J2 (bottom, mates Cypher-Plugboard)
```

---

## 2. J1 / J2 - Hub Connector Template

> **Connector Definition Owner:** this board. `J1` (top, male, `QTS-025-01-L-D-RA-P`) mates the
> Cypher Board's own hub connector. `J2` (bottom, female, `QSS-025-01-L-D-RA-K`) mates
> Cypher-Plugboard's own connector; identical pin map to `J1`.

| Top Row Signal | Top Pin# | Bottom Pin# | Bottom Row Signal |
| :--- | :---: | :---: | :--- |
| `3V3_ENIG` | 1 | 2 | `3V3_ENIG` |
| `3V3_ENIG` | 3 | 4 | `3V3_ENIG` |
| GND | 5 | 6 | GND |
| GND | 7 | 8 | GND |
| GND | 9 | 10 | GND |
| GND | 11 | 12 | GND |
| GND | 13 | 14 | GND |
| GND | 15 | 16 | GND |
| GND | 17 | 18 | `I2C_SDA` |
| GND | 19 | 20 | GND |
| `CPLD_RESET_N` | 21 | 22 | `I2C_SCL` |
| GND | 23 | 24 | GND |
| GND (bar) | 25 | 26 | GND (bar) |
| GND | 27 | 28 | GND |
| `TMS` | 29 | 30 | `TCK` |
| GND | 31 | 32 | GND |
| `TDI` | 33 | 34 | `TDO` |
| GND | 35 | 36 | GND |
| GND | 37 | 38 | GND |
| GND | 39 | 40 | GND |
| GND | 41 | 42 | GND |
| GND | 43 | 44 | GND |
| GND | 45 | 46 | GND |
| `3V3_ENIG` | 47 | 48 | `3V3_ENIG` |
| `3V3_ENIG` | 49 | 50 | `3V3_ENIG` |

**This board's wiring at `J1`:** `TDI` (pin 33) receives Cypher's own JTAG source. `TDO` (pin 34)
receives this board's own internal routing of whichever HID board's real TDO is currently the
Output-role board (see `Design_Spec.md §4`) - closing the loop back to Cypher. `I2C_SDA`/`I2C_SCL`
(pins 18/22) relay to `U1` and out to `J3`/`J4`. `CPLD_RESET_N`/`TMS`/`TCK` (pins 21/29/30)
broadcast out to `J2`, `J3`, and `J4`, terminated locally by `R1`-`R3`.

**This board's wiring at `J2`:** identical pin map, but `TDI`/`TDO` (pins 33/34) are left NC on
this side - all other signals (power, GND, `I2C_SDA`/`I2C_SCL`, `TMS`/`TCK`/`CPLD_RESET_N`) are
still relayed/broadcast here.

---

## 3. J3 / J4 - HID-Facing Connector Template

> **Connector Definition Owner:** this board. `J3` (left-upper, female, `QSS-025-01-L-D-RA-K`)
> mates whichever HID board is topmost; `J4` (left-lower, female, `QSS-025-01-L-D-RA-K`) mates
> whichever HID board is bottommost. Identical pin map on both.

| Top Row Signal | Top Pin# | Bottom Pin# | Bottom Row Signal |
| :--- | :---: | :---: | :--- |
| `3V3_ENIG` | 1 | 2 | `3V3_ENIG` |
| `3V3_ENIG` | 3 | 4 | `3V3_ENIG` |
| `I2C_SDA` | 5 | 6 | `I2C_SCL` |
| GND | 7 | 8 | GND |
| `RED_DRIVE_1_N` | 9 | 10 | `TCK` |
| `GREEN_DRIVE_1_N` | 11 | 12 | GND |
| `BLUE_DRIVE_1_N` | 13 | 14 | `TMS` |
| `ILLUMINATION_DRIVE_1_N` | 15 | 16 | GND |
| `RED_DRIVE_3_N` | 17 | 18 | `TDO_OUTPUT` |
| `GREEN_DRIVE_3_N` | 19 | 20 | GND |
| `BLUE_DRIVE_3_N` | 21 | 22 | `TDI_OUTPUT` |
| `ILLUMINATION_DRIVE_3_N` | 23 | 24 | `CPLD_RESET_N` |
| GND (bar) | 25 | 26 | GND (bar) |
| `CPLD_RESET_N` | 27 | 28 | `ILLUMINATION_DRIVE_2_N` |
| `TDI_INPUT` | 29 | 30 | `BLUE_DRIVE_2_N` |
| GND | 31 | 32 | `GREEN_DRIVE_2_N` |
| `TDO_INPUT` | 33 | 34 | `RED_DRIVE_2_N` |
| GND | 35 | 36 | `ILLUMINATION_DRIVE_4_N` |
| `TMS` | 37 | 38 | `BLUE_DRIVE_4_N` |
| GND | 39 | 40 | `GREEN_DRIVE_4_N` |
| `TCK` | 41 | 42 | `RED_DRIVE_4_N` |
| GND | 43 | 44 | GND |
| `I2C_SCL` | 45 | 46 | `I2C_SDA` |
| `3V3_ENIG` | 47 | 48 | `3V3_ENIG` |
| `3V3_ENIG` | 49 | 50 | `3V3_ENIG` |

**This board's wiring at `J3`/`J4` (identical on both):**

- All four colour-style signal groups (`RED`/`GREEN`/`BLUE`/`ILLUMINATION_DRIVE_{1,2,3,4}_N`) are
  driven from `U1`, identically on both connectors, regardless of which physical HID board is
  plugged into which connector.
- `TDI_INPUT`/`TDO_INPUT` (pins 29/33): broadcast/routed per `Design_Spec.md §4` - consumed by
  whichever HID board self-identifies as the Input-role board.
- `TDI_OUTPUT`/`TDO_OUTPUT` (pins 22/18): consumed by whichever HID board self-identifies as the
  Output-role board; `TDO_OUTPUT` is what this board internally routes back to `J1`'s own `TDO`
  pin.
- `TMS`/`TCK`/`CPLD_RESET_N` (pins 37/41/27, mirrored at 14/10/24): broadcast from `J1`,
  terminated locally by `R1`-`R3`.
- `I2C_SDA`/`I2C_SCL` (pins 5/6, mirrored at 46/45): relay to/from `J1` and feed `U1`.

---

## 4. PCB Stackup & Routing Notes

**Manufacturer:** JLCPCB
**Layer count:** 4-layer
**Stackup:** per GRS §2.3.1
**Copper:** 2oz outer
**Finish:** ENIG

| Layer | Role | Notes |
| :--- | :--- | :--- |
| L1 | Signals + components | Colour-style drive signals, I2C, JTAG |
| L2 | GND plane | Solid reference plane |
| L3 | Power | `3V3_ENIG` distribution |
| L4 | Secondary routing + silkscreen | Low-speed routing only |

### 4.1 Routing guidance

- Keep `I2C_SDA`/`I2C_SCL` as a matched short pair between `J1` and `U1`.
- Keep the JTAG termination resistors (`R1`-`R3`) close to their respective signal nets.
- Place one 100nF decoupler at `U1`'s supply pin.

---

## 5. Cross-References

| Document | Description |
| :--- | :--- |
| `design/Electronics/User_Settings_Module/Design_Spec.md` | Full electrical specification and BOM |
| `design/Electronics/Cypher/Board_Layout.md §4` | `J1` mating connector template ownership |
| `design/Electronics/Cypher-Plugboard/Board_Layout.md` | `J2` mating connector |
| `design/Electronics/Cypher-Input/Board_Layout.md`, `Cypher-Output/Board_Layout.md` | `J3`/`J4` mating connectors |

---

## 6. Mounting Holes

Mounting hole details are TBD at PCB Layout, deferred to
`.copilot/todos/usm-3-part-hid-module-mechanical-review.md`; the following provides a placeholder
for the assembly constraint.

### 6.1 Specifications

- **Count:** 4x M3 PTH mounting holes (one near each corner)
- **Hole diameter:** Ø3.2mm (clearance for M3 fastener)
- **Annular ring:** 6.0mm ENIG exposed pad (per GRS §4)
- **Net:** `GND_CHASSIS` — copper ring pads tied to chassis ground per GRS §4 (Mechanical Grounding)
- **BOM:** No BOM entry; plain chassis mounting holes with no fitted components

### 6.2 Positions

Follows GRS §4.3 Pattern A — exact XY positions TBD at PCB layout per GRS §4.2.

| Hole | Position Description |
| :--- | :--- |
| MH1 | Bottom-left corner |
| MH2 | Bottom-right corner |
| MH3 | Top-right corner |
| MH4 | Top-left corner |

> **Note:** Exact hole positions are subject to review at Schematic Capture and PCB Layout, once
> the mechanical mounting method is settled (see
> `.copilot/todos/usm-3-part-hid-module-mechanical-review.md`).

### 6.3 Cross-References

| Document | Relevance |
| :--- | :--- |
| `design/Standards/Global_Routing_Spec.md §4` | Mechanical grounding, ENIG annular ring, GND_CHASSIS bonding rules |
| `design/Electronics/User_Settings_Module/Design_Spec.md` | Full electrical specification; mounting hole DR TBD |
