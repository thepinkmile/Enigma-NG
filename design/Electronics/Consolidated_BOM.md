# Enigma-NG Consolidated BOM & Spares

## 1. Critical Spares (MOQ Recommendations)

* **Bourns AC72 TCO:** Order 5 (MOQ) - (2x Spares).
* **Eaton 15F Supercap:** Order 10 (MOQ) - (2x Spares + 2x Testing).
* **Samtec ERM8 (Gold):** Order 3 (MOQ) - (1x Spare).
* **Samtec ERF8 (Gold):** Order 3 (MOQ) - (1x Spare).
* **0.1% Thin-Film Resistors:** Order 50 (MOQ) - (High attrition risk).

## 2. Common Passives

* **0.1uF Decoupling:** Samsung CL10B104KB8NNNC (0603).
* **10uF Bulk:** Murata GRM188R61C106MA73D (0603).
* **10k Pull-ups:** Panasonic ERJ-3EKF1002V (0603).

## 3. Logic Passives  (0603 0.1% Thin-Film)

* **4.7kΩ:** 10 units (I2C-1 Telemetry Bus).
* **10kΩ:** 10 units (Reset & Battery Presence).
* **22Ω:** 10 units (USB 2.0 / JTAG Damping).

## 4. High-Speed Interconnects

* **Samtec ERM8-040-05.0-S-DV-K-TR (Male):** Power Module / Controller Beta.
* **Samtec ERF8-040-05.0-S-DV-K-TR (Female):** Controller Alpha / Stator.
* **Intel EPM240T100C5N:** 37 units (Standardized logic node).

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
| U10 | PoE ACF DC-DC Controller | TPS23730PWPR | TI WQFN-20; ACF topology, R_VFB set for 12V output | Mouser | 595-TPS23730PWPR | ~£3.50 | ~£2.00 |
| T2 | PoE ACF Isolation Transformer | **Coilcraft POE600F-12LD** | 60W; 12V out; 36–72V in; 200kHz; ACF topology; ≥1500Vrms; SMT; RoHS | Coilcraft Direct | POE600F-12LD | **£3.54** | **~£1.86** |

**Notes:**
- T2 is an **off-the-shelf catalogue part** — order direct from [coilcraft.com](https://www.coilcraft.com). 668 units confirmed in stock (Coilcraft Direct as of 2026-04-03).
- TPS23730 feedback resistors R_VFB must be calculated and verified against TI TPS23730 datasheet for 12V output regulation. Verify against Coilcraft POE600F-12LD application notes for operating point compatibility (turns ratio, duty cycle, magnetising inductance).
- OR-ing priority: TPS2372-4 `/PG` signal drives LM74700-Q1 enable on the USB-C path to enforce PoE source priority (PoE 12V < USB-C 15V passive OR-ing would otherwise prefer USB-C).

## 9. Suppliers

Reference information for placing orders with key component suppliers.

| # | Supplier | Role | Website | Notes |
| :--- | :--- | :--- | :--- | :--- |
| S01 | **Mouser Electronics** | Global distributor (primary) | [mouser.co.uk](https://www.mouser.co.uk) | Free next-day delivery on orders over £50. Wide TI/ADI/Microchip stock. Use part numbers from `Mouser Part #` column in board BOM tables. |
| S02 | **Farnell** | Global distributor (secondary UK) | [uk.farnell.com](https://uk.farnell.com) | Same-day dispatch for most stock lines. Good for Samtec, Würth, Bourns, Coilcraft. |
| S03 | **DigiKey** | Global distributor (USA-based, fast to UK) | [digikey.co.uk](https://www.digikey.co.uk) | Good for ADI (LTC3350), TI (low-MOQ), STMicroelectronics (STUSB4500). |
| S04 | **Coilcraft** | Transformer / inductor manufacturer | [coilcraft.com](https://www.coilcraft.com) | Order T2 (POE600F-12LD) direct from Coilcraft at coilcraft.com/en-us/. Minimum order 1 unit. Sample requests available. UK-friendly shipping. |
| S05 | **Texas Instruments** | IC manufacturer (TI store) | [ti.com/store](https://www.ti.com/store) | For TI parts (TPS2372-4, TPS23730, TPS25980, LMQ61460-Q1, LM74700-Q1, TPS25750, TPS7A8333P). Samples available via ti.com. |
| S06 | **Analog Devices (ADI)** | IC manufacturer | [analog.com](https://www.analog.com) | For LTC3350 supercap manager. Samples available. |
| S07 | **STMicroelectronics** | IC manufacturer | [st.com](https://www.st.com) | For STUSB4500 USB-C sink controller. Samples and eval kits available. |
| S08 | **Samtec** | Connector manufacturer | [samtec.com](https://www.samtec.com) | For ERF8/ERM8 80-pin BtB connectors. Order direct or via Farnell/Mouser. Min order typically 3 units. |
| S09 | **Würth Elektronik** | Passive / connector manufacturer | [we-online.com](https://www.we-online.com) | For RJ45 MagJack (7499111121A), EMI chokes (WE-CMBNC). Order via Farnell, Mouser, or direct. |
| S10 | **Molex** | Connector manufacturer | [molex.com](https://www.molex.com) | For battery connector (43045-0512 Micro-Fit 5-pin). Order via Mouser or DigiKey. |
| S11 | **Tecate Group** | Supercapacitor manufacturer | [tecategroup.com](https://www.tecategroup.com) | For TPLH-2R7/22WR12X31 22F/2.7V supercaps. May require broker/distributor sourcing — check Mouser or Newark. |
| S12 | **JLCPCB** | PCB fabrication & SMT assembly | [jlcpcb.com](https://www.jlcpcb.com) | Primary PCB manufacturer. Use JLCPCB Part # column for SMT assembly BOM upload. Stackup: JLC04201H-7628 (4-layer, 2oz). |
