# Enigma-NG Board Overview

**Status:** In Review
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Last Updated:** 2026-10-28

## 1. Overview

The Enigma-NG system uses a modular, museum-grade architecture built around a fixed Controller
motherboard and a set of removable/swappable modules: the Power Module; the Rotor Mini-Stack
(chained and reconfigurable depending on the required rotor count); and the Cypher-Input,
Cypher-Output, and Cypher-Plugboard HID-pair boards (each available in multiple variants —
e.g. 10-Numeric, 26-Char, 64-Char — swapped depending on the required configuration).

The `design/Standards/Global_Routing_Spec.md` applies to all boards except where a board-level design
spec explicitly records an exemption.

### 1.1 System Interconnect Diagram

![Cypher and Single Mini-Stack Configuration](../Diagrams/renders/cypher-and-single-stack-configuration.png)

*Full diagram source: [`design/Diagrams/cypher-and-stack-configuration-diagrams.drawio`](../Diagrams/cypher-and-stack-configuration-diagrams.drawio)*

## 2. Power Rail Glossary

- **3V3_ENIG**: Provided by a linear regulator on the Power Module. Powers all programmable logic
  (CPLD/FPGA), JTAG interface, I2C logic, rotor stack, and Controller digital I/O.
- **5V_MAIN**: Provided by the Power Module dual-buck stage. Powers the CM5 main supplies and the 5V
  system bus.
- **GND**: Common power and signal ground reference.
- **GND_CHASSIS**: Safety earth / EMI reference plane.
- **PWR_GD**: Direct PM -> Controller rail-health signal from a supervisor IC on the Power Module.

Only the Power Module implements the intentional `GND` ↔ `GND_CHASSIS` bond.

## 3. Telemetry Sensor Responsibility

- Power Module INA219 (`0x40`, `I2C0`): monitors `5V_MAIN`
- Cypher Board INA219 (`0x40`, `I2C1`): monitors rotor-stack `3V3_ENIG` (same address as the PM
  device — safe, since the two devices sit on independent I²C buses; see DEC-101)
- Power Module PCA9534A (`0x3F`, `I2C0`): virtualises PM status lines and SW1 RGB runtime control

## 4. I2C Bus Map

- `I2C0` (PM-dedicated) originates on the Controller and is routed to the Power Module over `J3`.
- `I2C1` (Cypher-local, active) and `I2C2` (Cypher-peripherals / USM / HID lighting, active)
  originate on the Controller and are routed to the Cypher Board over the signal-only dock `J5`,
  alongside `I2C3`/`I2C4`/`I2C6` (reserved for future expansion).
- Cypher Board -> User Settings Module over its Hub Connector Template (`J6`), relaying JTAG and
  `I2C2` onward from USM to both HID boards (Cypher-Input, Cypher-Output) and to Cypher-Plugboard.

> **Authoritative I2C address table:** see `Controller/Design_Spec.md §4.1` for the full list of
> device addresses, locations, and functions across all boards sharing these buses (Power
> Module, Cypher Board, User Settings Module, Cypher-Input). This section documents topology only,
> to avoid duplicating a table that must otherwise be kept in sync in two places.

## 5. System Architecture & Status

| Board Name | Role | Stackup | Status |
| :--- | :--- | :--- | :--- |
| **Controller Board** | Fixed motherboard; CM5 host; external RJ45, Ethernet ESD/magnetics, PoE front-end, HDMI, USB 3.0, and service docks for PM + Cypher Board | 6-Layer / 2oz | **In Review** |
| **Cypher Board** | Fixed backplane; fulfils the historical Stator, Reflector, JTAG-bridge, and electrical Plugboard roles in a single consolidated board; hosts rotor-stack and HID-pair docks plus its own Encoder Modules for the electrical Plugboard pass-through role | 6-Layer / 2oz | **In Review** |
| **Cypher-Input** | HID board; Keyboard role; one Encoder Module per key bank | 4-Layer / 2oz | **In Review** |
| **Cypher-Output** | HID board; Lightboard role; one Encoder Module per lamp bank | 4-Layer / 2oz | **In Review** |
| **Cypher-Plugboard** | Mechanical jack panel for the physical plugboard; the electrical Encoder Modules for this role live on the Cypher Board itself | 4-Layer / 2oz | **In Review** |
| **Encoder Module** | Generic daughterboard carrying one Programmable Hardware IC (CPLD/FPGA) and its required passive components; role (Keyboard / Lightboard / Plugboard pass) is set by the carrier board it mounts to, not by its own design. Mounts on the Cypher Board, Cypher-Input, and Cypher-Output | 4-Layer / 2oz | **In Review** |
| **Power Module** | Removable power-conditioning / UPS cartridge with supercaps, eFuse, OR-ing, USB-C input, battery input, and PM-local status expander | 6-Layer / 2oz | **In Review** |
| **Rotor Module** | Smart encryption units (up to 30x), each with a Programmable Hardware IC (CPLD/FPGA) | 4-Layer / 2oz | **In Review** |
| **Stack-Blanking** | Mandatory terminating panel for the final mini-stack in the chain | 4-Layer / 2oz | **In Review** |
| **Stack-Input** | Mini-stack input board; hosts the native Actuation Module MCU for local solenoid/motor actuation | 4-Layer / 2oz | **In Review** |
| **Stack-Interposer** | Chains two mini-stacks together, bridging power and JTAG between adjoining Stack-Output/Stack-Input pairs | 4-Layer / 2oz | **In Review** |
| **Stack-Output** | Mini-stack output board | 4-Layer / 2oz | **In Review** |
| **User Settings Module** | Panel-mount RGB colour / brightness / buzzer configuration interface, hosted off the Cypher Board's `I2C2` (Cypher-peripherals) bus | 4-Layer / 2oz | **In Review** |

## 6. Notes

- The Controller ↔ Power Module dock uses three TE 10-position 2.5mm connectors.
- The Controller ↔ Cypher Board dock uses a split power/signal pair: `J4` (Molex EXTreme Guardian
  HD hybrid, power-only) and `J5` (Samtec QSS/QTS-025, signal-only).
- Rotor / mini-stack interconnects use Samtec Edge-Rate (ERM8/ERF8) connectors.
- Enclosure-boundary connectors on the mini-stack boards (Stack-Input, Stack-Output,
  Stack-Interposer, Stack-Blanking) follow the flush(female)/protruding(male) mating convention in
  `Global_Routing_Spec.md §4.1a`; Rotor-facing connectors are excluded (internal to the assembly).
- All external I/O is grouped on the Controller side of the enclosure.
