# Checkpoint 036 — Settings Board Layout, BOM Audit, Switch Unification
**Date:** 2026-04-14
**Session:** <sanitized-session-id>
**Previous checkpoint:** 035-settings-board-dsi-provision-b.md

---
## Overview
This checkpoint covers completion of the Settings Board physical layout documentation, a full
system BOM deep-dive audit, unification of the Marquardt 1800 series rocker switch across the
Power Module and Settings Board, and cleanup of the Stator Board_Layout DIP switch references.
All design documentation is now fully consistent with the Settings Board (DEC-032) and DSI1
provision (DEC-033) features added in the previous checkpoint.

---
## Work Done
### Settings Board Board_Layout.md Created
`design/Electronics/Settings_Board/Board_Layout.md` — new file:

- ASCII component placement diagram (4-layer / 2oz copper, JLC04161H-7628)
- Component zone map: J_I2C (Zone A), U_EXP_SW_IN (Zone B), U_EXP_LED (Zone C), NPN transistors
  (Zone D)
- J_I2C 4-pin JST PH 2.0mm connector pinout table
- U_EXP_SW_IN (MCP23017 @ 0x26) full GPIO connection diagram with all pull-down resistor refs
- U_EXP_LED (MCP23017 @ 0x27) full GPIO connection diagram with base resistor refs
- LED colour-rail NPN transistor circuit diagram
- Switch-to-GPIO master wiring table (13 rows: 12 rockers + CFG_APPLY)
- 4-layer stackup table (L1 Signal / L2 GND / L3 3V3_ENIG / L4 GND + Data Plate)
- Trace width guidance table
### Settings Board BOM Completed
- `C_U_EXP_SW_IN` and `C_U_EXP_LED` (100nF X7R 0402) added to `Settings_Board/Design_Spec.md` BOM
- `J_I2C` JLCPCB PN correctly noted as TBD (C131342 is 3-pin B3B; 4-pin B4B PN unconfirmed)
- PCB stackup corrected: 4-layer JLC04161H-7628 / 2oz (was incorrectly set to 2-layer)
### BOM Deep-Dive Audit (background agent)
`Consolidated_BOM.md` updated:

- `SBD` column added to Component Usage Summary table
- MCP23017 total: STA=3, SBD=2 → system total = 5 ✓
- MMBT3904 ×4 row added (Settings Board only)
- PCA9685 (Stator U_EXP3) row added
- J_DSI1 (Controller) row added
- J_FAN (Controller) row added
- 0.1µF X7R cap and 10kΩ resistor totals updated for Settings Board passives
- J_I2C / J_CFG JLCPCB PN flagged as TBD
### Marquardt 1800 Switch Unification
All 13 RGB rocker switches unified to **Marquardt 1800 series SPDT latching rocker with RGB LED**
(MPN TBD). SPDT preferred to keep BOM component count minimal; SW1 (Power Module) unused pole NC
or shorted to active pole.

Files updated:

- `Power_Module/Design_Spec.md` — SW1 BOM row + prose updated (SPST → SPDT, open-item text removed)
- `Settings_Board/Design_Spec.md` — all 12 rocker switch BOM rows updated
- `Consolidated_BOM.md` — usage summary row: PM=1, SBD=12, total=13
### Stator Board_Layout DIP Switch Cleanup
`design/Electronics/Stator/Board_Layout.md` — SW1 and SW2 DIP switch sections removed and
replaced with:

- **J_CFG section** — 4-pin JST PH connector description, pinout table, note explaining DEC-032
  removal of DIP switches; R16–R25 pull-down placement notes retained
- **U_EXP4 section** — MCP23017 @ 0x22 placement guidance and full port/pin map

---
## Commits
| Hash | Message |
| :--- | :--- |
| `16bfc85` | Settings Board Board_Layout.md + BOM/stackup corrections |
| `dc7b3dd` | Fix Settings Board stackup: 2-layer → 4-layer JLC04161H-7628 |
| BOM audit commit | Consolidated BOM: SBD column, MCP23017×5, MMBT3904×4, J_DSI1, J_FAN |
| `4bec53b` | Unify rocker switch to Marquardt 1800 SPDT across PM + Settings Board |
| `bf6409f` | Stator Board_Layout: replace DIP switch sections with J_CFG + U_EXP4 |

---
## Known Correct (Do Not Flag in Review)
All items from checkpoint 035 known-correct list, plus:

- Settings Board stackup = 4-layer JLC04161H-7628 / 2oz (was temporarily 2-layer, corrected)
- SW1 (Power Module) now SPDT to match Settings Board rockers — unused pole NC, this is intentional
- Stator Board_Layout SW1/SW2 sections removed — correct, DIP switches replaced by Settings Board
- U_EXP4 @ 0x22 on Stator — correct, new expander added this session
- MCP23017 system total = 5 (STA×3 + SBD×2) — correct
- J_I2C / J_CFG JLCPCB PN = TBD — correct, 4-pin variant not yet confirmed

---
## TBD Parts (User to Research)
| Ref | Description | Constraint |
| :--- | :--- | :--- |
| SW1, SW_B1_EN, SW_B1[0:3], SW_B2_EN, SW_B2[0:5] | Marquardt 1800 series SPDT latching rocker, RGB LED, black body | All 13 must be same MPN |
| SW_CFG_APPLY | Panel-mount SPST NO momentary pushbutton | Quality feel preferred |
| R_LED_ANODE (×4) | 0603 anode current-limiting resistors — value TBD | Blocked on switch LED Vf/If spec |
| J_I2C / J_CFG | JST B4B-PH-K-S(LF)(SN) 4-pin 2.0mm — confirm JLCPCB PN | C131342 is 3-pin, 4-pin PN needed |
| J_DSI1 | 15-pin 1.0mm ZIF/FPC connector for CM5 DSI1 | Verify CM5 DSI1 pinout at schematic phase |

---
## Open Work Items
- OWI-001: Test coupons per board
- OWI-002: PAS definitions per board
- OWI-003: VHDL pseudo-code and CPLD config plans
- OWI-018: ENIG rib clearway bonding pad
- Deferred: ERA-3ARB2672V / ERA-3ARB1002V MOQ issue (R14/R15 LTC3350)
- KiCad setup documentation (lowest priority, placeholder for schematic phase)

---
## Next Steps
1. **Deep-dive review cycle** — full system review with datasheet access; fix any findings; 2
   consecutive clean passes required.
2. **Part searches** (user) — Marquardt 1800 SPDT variant MPN; SW_CFG_APPLY panel button;
   J_I2C/J_CFG 4-pin JST PH JLCPCB PN; J_DSI1 ZIF/FPC.
3. **R_LED_ANODE calculation** — once Marquardt 1800 LED Vf/If confirmed: R = (3.3V − Vf) / If.
4. **KiCad project setup** — when schematic phase begins.
