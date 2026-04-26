# Military Battery Connection Option

**Status:** Draft  
**Project:** Enigma-NG  
**Author:** Izzyonstage & GitHub Copilot  
**Version:** v.0.1.0  
**Associated Hardware Revision:** Rev A  
**Last Updated:** 2026-04-26

## 1. Purpose

This document captures a **candidate replacement** for the current Power Module smart-battery
connector. It exists to hold the military / NetWarrior-style option details separately from the
main Power Module design until the connector pin mapping, sourcing, and mechanical integration are
confirmed.

This is **not yet** the official Power Module battery connector.

## 2. Candidate Connector

| Item | Value |
| :--- | :--- |
| Manufacturer | Glenair |
| Candidate part | `807-216-00ZNU6-6DY` |
| Distributor / source | Heilind |
| Heilind SKU | `GLE807-216-00ZNU6-6DY` |
| Product page | <https://www.heilind.com/gle807-216-00znu6-6dy.html> |
| Reference datasheet markdown | [`Glenair-807-216-datasheet.md`](../../Datasheets/Glenair-807-216-datasheet.md) |
| Connector class | NetWarrior / military battery style circular connector |
| Contact count | 6 positions |
| Mounting style | Vertical PCB mount receptacle |
| Keying note | Trailing `Y` keying is the verified standard battery keying for this connector family and is specifically associated with LI-145 battery use |

## 3. Why This Option Exists

The currently documented Molex Micro-Fit battery connector remains electrically workable, but it is
not considered the preferred long-term fit for a rugged, quick-release, military-style external
battery interface.

The Glenair option is being explored because it is closer to the intended user experience:

- secure retention
- quick-disconnect battery cable handling
- a more professional soldier-power style connector ecosystem
- compatibility directionally aligned with NetWarrior / NATO battery-cable expectations

## 4. Current Integration Direction

### 4.1 Interposer concept

The chosen Glenair receptacle is a **vertical-mount connector**, while the Power Module battery
entry must still align with the rear external face near the USB-C connector.

The active preferred integration approach is therefore:

1. retain the rear-face battery entry location on the enclosure
2. place the Glenair receptacle on a **small dedicated interposer / daughterboard**
3. connect that interposer back to the main Power Module PCB rather than forcing the receptacle
   directly into the PM board outline

This keeps the main Power Module layout flexible and allows panel alignment to be solved cleanly.

### 4.2 Prototype-only adapter board

In addition to the future Power Module interposer, a **prototype-only battery adapter board** is
expected.

That prototype board should:

- use the same female Glenair receptacle candidate
- wire directly to the existing Accutronics / Inspired Energy smart-battery connector interface
- preserve the active 5-wire battery contract already defined by the Power Module
- live in a simple 3D-printed enclosure for cable / battery / mating validation

The purpose of that prototype unit is test and validation only; it is not part of the production
Power Module design.

## 5. Electrical Interface Notes

The active Power Module battery contract remains the existing 5-wire smart-battery interface:

| Logical signal | Current PM meaning |
| :--- | :--- |
| `VBATT+` | Battery positive input |
| `SMBUS_SCL` | Smart-battery clock |
| `SMBUS_SDA` | Smart-battery data |
| `BATT_PRES_N` | Battery-present sense derived from the battery auxiliary / `T` pin |
| `VBATT-` | Battery return |

The current Power Module assumption remains the selected Accutronics / Inspired Energy N205-family
battery behaviour where the `T` pin presents approximately **300 ohms to `VBATT-`** for presence
detection.

## 6. Pin-Mapping Caution

Initial downloaded material indicates that:

- connector pins **1** and **2** are documented for power / ground usage
- connector pins **4** and **5** are documented for SMBus data

However, the selected Glenair part is a **6-pin connector**, while the current Power Module battery
interface requires **5 logical signals**.

Therefore the exact contact assignment is currently **provisional** and must be confirmed before any
PCB is manufactured.

The connector keying itself is **not** provisional:

- `Y` keying has been verified as the standard battery keying for this connector family
- this keying is used so the connector cannot be mated to data-only ports on standard in-service
  devices such as STAR-PAN and STAR-PAN NG

### Required confirmation items

1. the exact pin numbering and contact function for all 6 positions
2. which contact should carry `BATT_PRES_N`
3. whether one position is intentionally unused, reserved, or dedicated by the cable standard
4. whether the selected mating cable assembly is confirmed as a minimum **5-signal** cable suitable
   for the Enigma-NG battery interface

## 7. Sourcing Rules

This candidate connector is currently treated as a **special-purpose part**.

For the active candidate state:

| Field | Current rule |
| :--- | :--- |
| DigiKey part number | Not available / not used |
| Mouser part number | Not available / not used |
| JLCPCB catalog part number | Not available |
| JLCPCB assembly mode | **Consignment only** |
| Primary source | Heilind |

This sourcing exception should remain explicit in the design docs if the part is later adopted.

## 8. Promotion Criteria

This connector option should only be rolled into the main Power Module design as the official
replacement once all of the following are complete:

1. Heilind / Glenair confirm the exact contact assignment for the chosen connector and cable
2. the interposer / daughterboard mechanical arrangement is proven to fit the rear face near USB-C
3. the prototype adapter board validates the battery electrical behaviour end-to-end
4. the Power Module design docs and BOM are updated together to replace the current Molex reference

## 9. Cross-References

| Document | Purpose |
| :--- | :--- |
| `design/Electronics/Power_Module/Design_Spec.md` | Main Power Module electrical specification |
| `design/Datasheets/Glenair-807-216-datasheet.md` | Combined markdown extraction of the Glenair drawing PDF and 807 NW catalogue PDF |
| `design/Mechanical/Power_Module/Design_Spec.md` | Power Module external-face and connector clearance context |
