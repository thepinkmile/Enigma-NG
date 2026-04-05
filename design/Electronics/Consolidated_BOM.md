# Enigma-NG Consolidated BOM & Spares

**Status:** Draft — pending schematic freeze
**Version:** v1.0.0
**Last Updated:** 2026-04-04

## Overview

This is the consolidated Bill of Materials for all boards and modules in the Enigma-NG system.
It covers critical spares, common passives, high-speed interconnects, power components, and supplier
reference information. For per-board BOM notes and design constraints, refer to each board's
individual `Design_Spec.md` file.

## 1. Critical Spares (MOQ Recommendations)

* **Bourns AC72 TCO:** Order 5 (MOQ) - (2x Spares).
* **Eaton 15F Supercap:** Order 10 (MOQ) - (2x Spares + 2x Testing).
* **Samtec ERM8-040 (Gold, 80-pin):** Order 3 (MOQ) — Power Module J1, (1× Spare). Order separately from ERM8-020.
* **Samtec ERM8-020 (Gold, 40-pin):** Order 3 (MOQ) — Stator J1, (1× Spare). Poka-yoke pair with ERF8-020.
* **Samtec ERF8-040 (Gold, 80-pin):** Order 3 (MOQ) — Controller J1, (1× Spare).
* **Samtec ERF8-020 (Gold, 40-pin):** Order 3 (MOQ) — Controller J2, (1× Spare). Poka-yoke pair with ERM8-020.
* **0.1% Thin-Film Resistors:** Order 50 (MOQ) - (High attrition risk).

## 2. Common Passives

* **0.1uF Decoupling:** Samsung CL10B104KB8NNNC (0603).
* **10uF Bulk:** Murata GRM188R61C106MA73D (0603).
* **10k Pull-ups:** Panasonic ERJ-3EKF1002V (0603).

## 3. Logic Passives  (0603 0.1% Thin-Film unless otherwise noted)

* **4.7kΩ:** 10 units (I2C-1 Telemetry Bus).
* **10kΩ:** 10 units (Reset, Battery Presence & ROTOR_EN pull-up to 3V3_ENIG).
* **22Ω:** 10 units (USB 2.0 / JTAG Damping).
* **121kΩ:** 5 units (TPS2372-4 RMPS — MPS current set, R13).
* **301Ω:** 5 units (LTC3350 RICHARGE — charge current set, R11).
* **10mΩ / 5A (2512 Kelvin):** 5 units (LTC3350 RSENSE — charge path current sense, R12; Bourns CSS2H-2512R-**R010**ELF).

## 3a. EMI Filter Passives

| Ref | Component | Part | Value | Package | Mouser Part # |
| :--- | :--- | :--- | :--- | :--- | :--- |
| L1 | EMI Primary CMC (broadband CM) | Würth WE-CMBNC 7448031002 | 2mH, 10A, nanocrystalline | THT 24×17×25mm | 710-7448031002; alt: Newark 75X1218 |
| L2 | EMI Secondary CMC (HF, >10MHz) | Würth WE-CMBNC 7448031002 (**replaces discontinued Laird CM5022**) | 2mH, 10A, nanocrystalline | THT 24×17×25mm | 710-7448031002; alt: Newark 75X1218 |
| L3 | EMI DM Pi-filter Inductor | Bourns SRP1265A-100M (replaces Würth 7447789100 — not in public catalog) | 10µH, 15.5A Isat, DCR 16.5mΩ | 13.5×12.5×6.2mm SMT ⚠️ footprint change | 652-SRP1265A-100M; alt: Farnell ~2741 in stock |
| C1, C4 | Pi-filter bulk cap (2× each) | Samsung CL32B226KAJNNNE | 22µF 25V X7R | 1210 | 187-CL32B226KAJNNNE |
| C2, C5 | Pi-filter mid-freq bypass (2× each) | Murata GRM21BR71H105KA12L | 1µF 50V X7R | 0805 | 81-GRM21BR71H105KA2L |
| C3, C6 | Pi-filter HF bypass (2× each) | Samsung CL05B104KB5NNNC | 100nF 50V X7R | 0402 | 187-CL05B104KB5NNNC |
| C7–C12 | Power IC bulk caps (U1 in/out, U2A in/out, U2B in/out) | Samsung CL32B226KAJNNNE | 22µF 25V X7R | 1210 | 187-CL32B226KAJNNNE |
| C13 | LDO input cap (U7 VIN) | Murata GRM31CR72E106KA12L | 10µF 25V X7R | 1206 | 81-GRM31CR72E106KA12L |
| C14 | LDO output cap (U7 VOUT) | Samsung CL32B226KAJNNNE | 22µF 25V X7R | 1210 | 187-CL32B226KAJNNNE |
| C15–C22 | IC VCC bypass (U3–U6, U8–U11) | Samsung CL05B104KB5NNNC | 100nF 50V X7R | 0402 | 187-CL05B104KB5NNNC |
| C23 | MIC1555 timing cap (C_OSC) | Murata GRM21BR71H105KA2L | 1µF 50V X7R | 0805 | 81-GRM21BR71H105KA2L |
| C24 | TPS23730 soft-start cap (C_SS) | Samsung CL05B103KB5NNNC | 10nF 50V X7R | 0402 | 187-CL05B103KB5NNNC |

**Pi-filter performance summary (f_c = 10.5kHz):**

* −46dB DM attenuation at 150kHz (EN 55032 Class B lower edge) ✓
* −51dB at 200kHz (TPS23730 ACF switching frequency) ✓
* −63dB at 400kHz (LMQ61460-Q1 buck switching frequency) ✓

## 4. High-Speed Interconnects

* **Samtec ERM8-040-05.0-S-DV-K-TR (Male, 80-pin):** Power Module J1 (Link-Alpha).
* **Samtec ERM8-020-05.0-S-DV-K-TR (Male, 40-pin):** Stator J1 (Link-Beta).
* **Samtec ERF8-040-05.0-S-DV-K-TR (Female, 80-pin):** Controller J1 (Link-Alpha).
* **Samtec ERF8-020-05.0-S-DV-K-TR (Female, 40-pin):** Controller J2 (Link-Beta).
* **Intel EPM240T100C5N:** 37 units (Standardized logic node).

## 4a. Encoder Board — Plugboard Jacks, Keyboard Switches & PCB Spade Terminals

| Ref | Component | Part / Description | Qty | Supplier | Supplier Ref / Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| J1 (×64) | Stecker jack sockets | 6.35mm (¼″) mono switched panel-mount jack — Tip: ENC signal path; Switch contact: insertion-detect (→ CPLD INT); Sleeve: GND direct. **Already purchased.** | 64 | SaiBuy.Ltd (eBay) | eBay item 334364197440 — £1.66/unit (sold in packs of 3 for £4.99). [ebay.co.uk — SaiBuy.Ltd](https://www.ebay.co.uk/str/saibuyltd) |
| SW1-64 | Keyboard switches | DPDT 6-pin momentary push button — Pole 1 electrically active: COM1+NO1 → key-press to CPLD. Pole 2 pins soldered for mechanical key anchoring only (no electrical connection). NC1 not connected. Keys connect to keyboard Encoder board only; no direct switch connection to Lightboard. **Already purchased.** | 64 | gadgetkingdom (eBay) | Sold in packs of 2. Listing title: "Mechanical Push Button Switch DPDT 2 Pole 6 Pin 1 Position 2pcs". |
| BT1-64 | PCB blade terminals — ENC signal (Row 1) | Keystone 1285 — 6.35mm (0.250″) straight vertical PCB-mount male blade tab, through-hole. Accepts 6.35mm female crimp spade from jack Tip harness. | 64 | Mouser / DigiKey | Mouser: 534-1285 · DigiKey: 36-1285-ND |
| BT65-128 | PCB blade terminals — INT detect (Row 2) | Keystone 1285 — same part. Accepts 6.35mm female crimp spade from jack Switch contact harness. | 64 | Mouser / DigiKey | Mouser: 534-1285 · DigiKey: 36-1285-ND |
| BT129-192 | PCB blade terminals — KEY_COM (Row 3) | Keystone 1285 — same part. Switch COM1 lines; accept 6.35mm female crimp spade from keyboard harness. | 64 | Mouser / DigiKey | Mouser: 534-1285 · DigiKey: 36-1285-ND |
| BT193-256 | PCB blade terminals — KEY_NO (Row 4) | Keystone 1285 — same part. Switch NO1 lines; CPLD key-press inputs (active-low via pull-up). | 64 | Mouser / DigiKey | Mouser: 534-1285 · DigiKey: 36-1285-ND |

**Notes:**

* **Plugboard jacks (J1 ×64):** mount in the plugboard panel. Each jack connects via a 2-wire harness (Tip + Switch contact; Sleeve to chassis GND). Rows 1–2 (BT1–128).
* **Keyboard switches (SW1-64):** mount in the keyboard panel. Each switch connects via a 2-wire harness (COM1 + NO1 from Pole 1 only). Pole 2 pins are mechanically soldered for physical anchoring
  — no electrical connection. Keys connect to the keyboard Encoder board only; no direct switch wiring to the Lightboard. Rows 3–4 (BT129–256).
* **Total PCB blade terminals: 256** — four rows of 64, all Keystone 1285.
* Stecker patch cables (plugboard) use 6.35mm mono jack plugs (TS) — not included in BOM; customer-supplied.

## 5. Controller Specifics

* **CM5 Module:** Raspberry Pi SC1180 (8GB/32GB/Wireless).
* **Stacked USB 3.0:** Molex 48406-0003 (THT Right-Angle).
* **Full HDMI:** TE Connectivity 2007435-1 (THT Type-A).

### 5.1. Controller User I/O Protection

* **TPS2065CDBVR:** USB Power Distribution Switch (SOT-23-5) (1.6A Limit).
* **AP2331W-7:** HDMI Current Limiter (SOT-25) (50mA Limit).
* **TPD4E05U06DQNR:** 4-Channel ESD Protection (U-DFN1010-10).

## 6. Backplane & Extension Components

* **40-Pin Box Header (Vertical):** Harting 09185406914 or equivalent (4x per Stator).
* **20-Pin Box Header (Vertical):** 2.54mm Gold-plated Shrouded (2x per Extension/Reflector).
* **12-Pin Box Header (Vertical):** 2.54mm Gold-plated Shrouded (1x per Stator/Rotor).
* **10-Pin Box Header (Vertical):** 2.54mm Gold-plated Shrouded (1x per Stator/Rotor).
* **8-Pin Box Header (Vertical):** 2.54mm Gold-plated Shrouded (1x per Stator/Rotor).
* **Copper Shielding Tape:** 50mm (2.0") Conductive Adhesive (Manual cable wrap).

## 7. Power & Telemetry Sensors

* **INA219AIDR:** 1 unit (Stator Board - 0x45).
* **20mΩ 0805 Shunt:** 2 units (Stator Load / Spare).

## 8. Power Module — PoE Subsystem

| Ref | Component | Part Number | Value / Notes | Supplier | Supplier Part # | Unit Price (1-off) | Unit Price (volume) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| U9 | PoE PD Interface (Type 4) | TPS2372-4RGWR | TI QFN-16; 802.3bt Type 4, external hotswap, up to 90W | Mouser | 595-TPS2372-4RGWR | ~£3.50 | ~£2.00 |
| U10 | PoE ACF DC-DC Controller | TPS23730RMTR | TI WQFN-20; ACF topology; PSR mode; 12V output set by POE600F-12LD turns ratio; VS pin to aux winding | Mouser | 595-TPS23730RMTR | ~£3.50 | ~£2.00 |
| T2 | PoE ACF Isolation Transformer | **Coilcraft POE600F-12LD** | 60W; 12V out; 36–72V in; 200kHz; ACF topology; ≥1500Vrms; SMT; RoHS | Coilcraft Direct | POE600F-12LD | **£3.54** | **~£1.86** |
| R13 | TPS2372-4 RMPS (MPS current set) | 121kΩ 0.1% Thin-Film | 121kΩ E96; IMPS = VIMPS/RMPS = 1.205V/121kΩ = 9.96mA (Type 4 MPS auto-stretch) | Mouser | 667-ERJ-3EKF1213V | ~£0.10 | ~£0.03 |

**Notes:**

* T2 is an **off-the-shelf catalogue part** — order direct from [coilcraft.com](https://www.coilcraft.com). 668 units confirmed in stock (Coilcraft Direct as of 2026-04-03).
* TPS23730 operates in **PSR (Primary-Side Regulation) mode** using the auxiliary winding of the POE600F-12LD. No external TL431 or optocoupler required.
* TPS2372-4 uses **Autoclass** for automatic 4-event IEEE 802.3bt Type 4 classification; no external RCLASS resistor required. R13 (RMPS) programs MPS pulse current only.
* OR-ing priority: TPS2372-4 `/PG` signal drives LM74700-Q1 enable on the USB-C path to enforce PoE source priority.

## 9. Power Module — IC & Connector BOM (Multi-Distributor)

> **Legend:** ✓ = confirmed from distributor search · ~ = derived from manufacturer prefix convention · ⚠️ = part number issue flagged · — = not stocked / THT not assembled

| Designator | Part | Package | Mouser # | DigiKey # | JLCPCB # | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| U3 | LTC3350EUHF#PBF | QFN-38 5×7 | 584-LTC3350EUHF#PBF ✓ | 1469-1010-1-ND (tube) / **1469-1010-2-ND** (T&R) | — (not in library) | ~4.5k in stock Mouser (tube). T&R variant has ~7.5k DigiKey stock. JLCPCB custom-supply only. |
| U5 | STUSB4500LQTR | QFN-24 4×4 | 511-STUSB4500LQTR ~ | 497-STUSB4500LQTRCT-ND ~ ⚠️ verify | C841785 (non-L variant STUSB4500QTR — STUSB4500LQTR may not be in JLCPCB catalog) | Primary PN: STUSB4500LQTR (lower Iq ~160µA). If OOS, use STUSB4500QTR as alternative (non-L variant, ~210µA Iq, pin-compatible). |
| U6 | ~~LM74700-Q1DCKR~~ → **LM74700QDBVRQ1** | SOT-23-6 (DBV) | 595-LM74700QDBVRQ1 ~ | **296-LM74700QDBVRQ1CT-ND** ✓ | — (extended) | ⚠️ **BOM PART NUMBER INCORRECT** — LM74700-Q1DCKR does not exist. Correct automotive part is LM74700QDBVRQ1 (DBV=SOT-23-6 package, not DCK/SC70). DigiKey 35k+ in stock. |
| U8 | MCP121T-450E/LB | SC70-3 | 579-MCP121T-450ELB ~ | **MCP121T-450E/LBCT-ND** ✓ | — (extended) | DigiKey 2.3k in stock @ $0.53/1. SC70-3 = compact 3-pin package. Microchip prefix 579-. |
| U1 | TPS259803ONRGER | VQFN-24 (RGE) | 595-TPS259803ONRGER ~ | 296-TPS259803ONRGERCT-ND ~ ⚠️ verify | — | 16.9V OVLO variant. Mouser/DigiKey PNs approximate — verify before ordering. Replaces placeholder TPS25980RPWR. |
| U2A/U2B | LMQ61460ARUMR | WSON-8 2×2 | **595-LMQ61460ARUMR** (provided) | 296-LMQ61460ARUMR-ND ~ | — | ⚠️ Not found on findchips; similar family variant LMQ61460AASRJRR available (296-LMQ61460AASRJRRCT-ND, different WSON variant). Verify RUMR suffix with TI/Mouser before ordering. |
| U4 | TPS25751DREFR | WQFN-38 6×4mm | 595-TPS25751DREFR | TPS25751DREFR-ND | — | ✅ Replaces NRND TPS25750DRCR (see DEC-012). PD3.1 certified (USB-IF TID#10306). ⚠️ Package changed from QFN-28 to WQFN-38 — schematic symbol and PCB footprint update required. |
| U7 | TPS7A8333PRMWR | WSON-12 | 595-TPS7A8333PRMWR ~ | 296-TPS7A8333PRMWR-ND ~ ⚠️ verify | — | Fixed 3.3V, WSON-12. Harmonized with Design_Spec primary PN. Mouser/DigiKey approximate — verify before ordering. |
| U9 | TPS2372-4RGWR | VQFN-20 | **595-TPS2372-4RGWR** (provided) | **296-52795-1-ND** ✓ | — (extended) | DigiKey temporarily out of stock (~6-week lead time). $3.09/1. VQFN-20 per TI. |
| U10 | TPS23730PWPR | HTSSOP-20 (PWP) | **595-TPS23730PWPR** (provided) | 296-TPS23730PWPR-ND ~ | — | ⚠️ **PACKAGE DISCREPANCY** — TI product page shows TPS23730 in VQFN-45 (RMT 7×5mm). PWP suffix = PowerPAD HTSSOP-20. These cannot be the same; verify correct package variant. WQFN-20 variant is TPS23730RMTR (296-TPS23730RMCT-ND, ~5.6k in stock). |
| D2 | TPD2E2U06DRLR | SOT-553 (DRL) | **595-TPD2E2U06DRLR** ✓ | **296-38361-1-ND** ✓ | — (extended) | DigiKey 1.4k in stock @ $0.41/1. Dual-channel SMBus ESD, 5.5V. Part confirmed to exist. Farnell stocked (3116500). |
| J2 | Würth 7499111121A | THT RJ45 | **710-7499111121A** ✓ | **1297-1070-5-ND** ✓ | — (THT) | Mouser ~191, DigiKey ~879 in stock. ~$8.41/1 (Mouser), ~$8.41/1 (DigiKey). Farnell out of stock. JLCPCB does not stock THT MagJacks — hand-place or pre-fit. |
| J3 | Molex 43650-0519 | THT Micro-Fit 3.0 | 538-43650-0519 ~ | WM7843-ND ⚠️ verify | — (THT) | ⚠️ **MPN corrected** — `43045-0512` does not exist. Correct series is `43650` (vertical THT). 43650-0519: 5-circuit, 1-row, gold contacts, board lock, 3mm pitch. Farnell ~1143 in stock. DigiKey WM7843-ND inferred; **verify exact WM number**. JLCPCB does not stock THT connectors. |
| J4 | GCT USB4135-GF-A | SMT vertical 8.94×3.5mm | 640-USB4135-GF-A | 2073-USB4135-GF-A-ND | — (hand-place) | 24-pin USB Type-C receptacle, 5A VBUS, CC1/CC2 included. Connects to STUSB4500 (U5) for 15V PD negotiation. Not in JLCPCB standard catalog; hand-place or pre-fit. |
| Q1, Q2, Q3 | TI CSD17483F4T (×3) | SON-8 3.3×3.3mm | 595-CSD17483F4T | 296-CSD17483F4TCT-ND | — | N-ch MOSFET, 30V, 10A, 8.4mΩ. Driven by LM74700-Q1 (U6) for triple-input ideal-diode OR-ing (PoE / USB-C / Battery). One per input path. ⚠️ Verify U6 instance count — LM74700-Q1 controls one FET per IC; three inputs may require three U6 instances at schematic capture. |
| R14, R15 | Panasonic ERA-3ARB series | 0603 0.1% Thin-Film | See PN below | See PN below | — | BACKUP pin voltage divider for LTC3350 (U3). R14=30.1kΩ (ERA-3ARB3012V, Mouser 667-ERA-3ARB3012V, DigiKey P30.1KBYCT-ND). R15=10.0kΩ (ERA-3ARB1002V, Mouser 667-ERA-3ARB1002V, DigiKey P10.0KBYCT-ND). Sets BACKUP trigger at 4.81V. |
| U11 | MIC1555YM5-TR | SOT-23-5 | 579-MIC1555YM5TR | MIC1555YM5-TRCT-ND | C431119 | CMOS timer IC (Microchip). 1Hz hardware status LED oscillator. R16=10kΩ (ERA series), R17=715kΩ (ERJ-3EKF7153V, Mouser 667-ERJ-3EKF7153V), C23=1µF (same Murata as C2/C5). |
| R18–R21 | RJ45 Bob Smith termination resistors (×4) | 75Ω ±1% 0402 | 0402 | 667-ERJ-2RKF75R0V | P75.0BYCT-ND | C105872 |
| C25 | RJ45 Bob Smith termination capacitor (⚠️ Y1-class 0402 is rare; 100V X7R acceptable proxy for EMC at board level) | 10nF 100V X7R 0402 | 0402 | 81-GRM155R72A103KA35D | 490-GRM155R72A103KA35DCT-ND | C57112 |

### 9.0. Part Number Issues Requiring Action

1. **U6** — Replace `LM74700-Q1DCKR` with **`LM74700QDBVRQ1`** everywhere in schematics and BOM. The DCK (SC70) package does not exist for this part; DBV (SOT-23-6) is the correct package.
2. **U10** — Confirm whether TPS23730 in **PWP (HTSSOP-20)** or **RMT (VQFN-45)** or **RMTR (WQFN-20)** is the intended package. The BOM says "WQFN-20" which matches RMTR — update MPN accordingly.
3. **U1** — Updated to `TPS259803ONRGER` (16.9V OVLO VQFN-24 variant). Mouser/DigiKey approximate; verify before ordering.
4. **U4** — Replaced with TPS25751DREFR (WQFN-38 6×4mm). See DEC-012. ⚠️ Schematic and PCB footprint update required (package change from QFN-28).

## 10. Suppliers

Reference information for placing orders with key component suppliers.

| # | Supplier | Role | Website | Notes |
| :--- | :--- | :--- | :--- | :--- |
| S01 | **Mouser Electronics** | Global distributor (primary) | [mouser.co.uk](https://www.mouser.co.uk) | Free next-day delivery on orders over £50. Wide TI/ADI/Microchip stock. Use part numbers from `Mouser Part #` column in board BOM tables. |
| S02 | **Farnell** | Global distributor (secondary UK) | [uk.farnell.com](https://uk.farnell.com) | Same-day dispatch for most stock lines. Good for Samtec, Würth, Bourns, Coilcraft. |
| S03 | **DigiKey** | Global distributor (USA-based, fast to UK) | [digikey.co.uk](https://www.digikey.co.uk) | Good for ADI (LTC3350), TI (low-MOQ), STMicroelectronics (STUSB4500). |
| S04 | **Coilcraft** | Transformer / inductor manufacturer | [coilcraft.com](https://www.coilcraft.com) | Order T2 (POE600F-12LD) direct from Coilcraft at coilcraft.com/en-us/. Minimum order 1 unit. Sample requests available. UK-friendly shipping. |
| S05 | **Texas Instruments** | IC manufacturer (TI store) | [ti.com/store](https://www.ti.com/store) | For TI parts (TPS2372-4, TPS23730, TPS25980, LMQ61460-Q1, LM74700-Q1, TPS25751DREFR, TPS7A8333P). Samples available via ti.com. |
| S06 | **Analog Devices (ADI)** | IC manufacturer | [analog.com](https://www.analog.com) | For LTC3350 supercap manager. Samples available. |
| S07 | **STMicroelectronics** | IC manufacturer | [st.com](https://www.st.com) | For STUSB4500 USB-C sink controller. Samples and eval kits available. |
| S08 | **Samtec** | Connector manufacturer | [samtec.com](https://www.samtec.com) | For ERF8/ERM8 BtB connectors (80-pin Link-Alpha, 40-pin Link-Beta). Order direct or via Farnell/Mouser. Min order typically 3 units. |
| S09 | **Würth Elektronik** | Passive / connector manufacturer | [we-online.com](https://www.we-online.com) | For RJ45 MagJack (7499111121A), EMI chokes (WE-CMBNC). Order via Farnell, Mouser, or direct. |
| S10 | **Molex** | Connector manufacturer | [molex.com](https://www.molex.com) | For battery connector (43650-0519 Micro-Fit 3.0, 5-pin vertical THT). Order via Mouser or DigiKey. |
| S11 | **Tecate Group** | Supercapacitor manufacturer | [tecategroup.com](https://www.tecategroup.com) | For TPLH-2R7/22WR12X31 22F/2.7V supercaps. May require broker/distributor sourcing — check Mouser or Newark. |
| S12 | **JLCPCB** | PCB fabrication & SMT assembly | [jlcpcb.com](https://www.jlcpcb.com) | Primary PCB manufacturer. Use JLCPCB Part # column for SMT assembly BOM upload. Stackup: JLC04201H-7628 (4-layer, 2oz). |
| S13 | **Newark (Avnet)** | Global distributor (UK stock) | [newark.com](https://www.newark.com) | Good for Würth passives with immediate UK stock. L1/L2 WE-CMBNC 7448031002 available as Newark #75X1218 (~561 pcs, ~$14.58 each). Same-group as Farnell/element14. |

---

## 11. Datasheet Links

Product page links for all major components for design review and procurement verification.

| Ref | Part / Description | Manufacturer | Product Page |
| :--- | :--- | :--- | :--- |
| U1 | TPS25980 — eFuse / Ideal Diode (16.9V OVLO) | Texas Instruments | [ti.com/product/TPS25980](https://www.ti.com/product/TPS25980) |
| U2A, U2B | LMQ61460-Q1 — 6A Synchronous Buck Converter | Texas Instruments | [ti.com/product/LMQ61460-Q1](https://www.ti.com/product/LMQ61460-Q1) |
| U3 | LTC3350 — Supercap Manager / Charger / Backup | Analog Devices | [analog.com/en/products/ltc3350.html](https://www.analog.com/en/products/ltc3350.html) |
| U4 | TPS25751 — USB PD 3.1 DRP Controller | Texas Instruments | [ti.com/product/TPS25751](https://www.ti.com/product/TPS25751) |
| U5 | STUSB4500 — USB-C Sink PD Negotiation Controller | STMicroelectronics | [st.com/en/interfaces-and-transceivers/stusb4500.html](https://www.st.com/en/interfaces-and-transceivers/stusb4500.html) |
| U6 | LM74700-Q1 — Ideal Diode OR-ing Controller | Texas Instruments | [ti.com/product/LM74700-Q1](https://www.ti.com/product/LM74700-Q1) |
| U7 | TPS7A8333P — 3.3V 3A LDO Regulator (3V3_ENIG) | Texas Instruments | [ti.com/product/TPS7A8333](https://www.ti.com/product/TPS7A8333) |
| U8 | MCP121T-450E — 4.50V Voltage Supervisor | Microchip Technology | [microchip.com/en-us/product/MCP121T](https://www.microchip.com/en-us/product/MCP121T) |
| U9 | TPS2372-4 — IEEE 802.3bt PoE PD Controller | Texas Instruments | [ti.com/product/TPS2372-4](https://www.ti.com/product/TPS2372-4) |
| U10 | TPS23730 — ACF PoE+ DC/DC Controller | Texas Instruments | [ti.com/product/TPS23730](https://www.ti.com/product/TPS23730) |
| T2 | POE600F-12LD — Active Clamp Flyback Transformer | Coilcraft | [coilcraft.com/…/poe600f](https://www.coilcraft.com/en-us/products/power-magnetics/power-transformers/poe-transformers/poe600f/) |
| L1, L2 | WE-CMBNC 7448031002 — Nanocrystalline CMC | Würth Elektronik | [we-online.com (search 7448031002)](https://www.we-online.com/en/components/products/CMBNC) |
| L3 | SRP1265A-100M — 10µH 14A Power Inductor | Bourns | [bourns.com/…/SRP1265A](https://www.bourns.com/products/inductors/power-inductors/product/SRP1265A) |
| R12 / R_SENSE | CSS2H-2512R-R010ELF — 10mΩ Current Sense Resistor | Bourns | [bourns.com/…/CSS2H](https://www.bourns.com/products/resistors/current-sense-resistors/product/CSS2H) |
| J2 | 7499111121A — GbE RJ45 MagJack with LEDs | Würth Elektronik | [we-online.com (search 7499111121A)](https://www.we-online.com/en/components/products/GMJT) |
| J3 | 43650-0519 — Micro-Fit 3.0, 5-pin Vertical THT | Molex | [molex.com/…/436500519](https://www.molex.com/en-us/products/part-detail/436500519) |
| J4 | USB4135-GF-A — USB Type-C SMT Receptacle, 5A | GCT | [gct.co/part/USB4135-GF-A](https://gct.co/part/USB4135-GF-A) |
| Q1–Q3 | CSD17483F4T — N-ch MOSFET 30V/10A, SON-8 | Texas Instruments | [ti.com/product/CSD17483F4](https://www.ti.com/product/CSD17483F4) |
| U11 | MIC1555 — CMOS Timer, SOT-23-5 | Microchip Technology | [microchip.com/en-us/product/MIC1555](https://www.microchip.com/en-us/product/MIC1555) |
| C_SC1–4 | TPLH-2R7/22WR12X31 — 22F / 2.7V Supercapacitor | Tecate Group | [tecategroup.com (search TPLH-2R7-22WR)](https://www.tecategroup.com/ultracapacitors-supercapacitors/) |
| F1 | AC72ABD — 72°C SMD Thermal Cutoff (TCO) | Bourns | [bourns.com/products/fusescircuit-protection/thermally-sensitive-devices/product/AC72](https://www.bourns.com/products/fusescircuit-protection/thermally-sensitive-devices/product/AC72) |
| D1 | TPD1E10B06 — Single-Channel 10V TVS ESD (BATT_PRES) | Texas Instruments | [ti.com/product/TPD1E10B06](https://www.ti.com/product/TPD1E10B06) |
| D2 | TPD2E2U06 — Dual-Channel 5.5V SMBus ESD (Battery SMBus) | Texas Instruments | [ti.com/product/TPD2E2U06](https://www.ti.com/product/TPD2E2U06) |
| D3, D4, D5 | TPD4E05U06 — 4-Channel 5V ESD Array (USB-C / RJ45 MDI) | Texas Instruments | [ti.com/product/TPD4E05U06](https://www.ti.com/product/TPD4E05U06) |
| J1 (Link-Alpha) | ERM8-040 / ERF8-040 — 80-pin 0.5mm-pitch BtB Connector | Samtec | [samtec.com/products/erm8](https://www.samtec.com/products/erm8) |
| J2 (Link-Beta) | ERM8-020 / ERF8-020 — 40-pin 0.5mm-pitch BtB Connector | Samtec | [samtec.com/products/erm8](https://www.samtec.com/products/erm8) |
