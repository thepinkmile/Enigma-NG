Committed (`70689cf`). Now the summary and reprinted list from #28:

---

<overview>
The session completed the full Enigma-NG system design review cycle (R1–R9), corrected two errors introduced by the review itself (wrong eFuse MPN, wrongly removed R1 package), then compiled a master parts list for the user's manual component verification. The user provided verified supplier PNs and datasheet files for components #1–#27, identified several incorrect or invalid MPNs, and requested all corrections be applied to the design files plus a reprint of the list from #28 onwards.
</overview>

<history>
1. **Session context**: Full system review cycle (R1–R9) completed, yielding 2 clean passes. Checkpoint 020 created. User identified two errors: eFuse MPN (TPS259807 should be TPS259804) and Reflector R1 0603 package wrongly removed. Agent `revert-efuse-r1-fixes` completed these corrections (commit `7e165cb`).
2. **User requested all components in a single master list** — compiled and printed covering all 100 component types across 10 boards with Mouser/DigiKey/JLCPCB PNs and online datasheet links.
3. **User verified #1–#27 and provided corrections:**
   - LTC3350: DigiKey→505-LTC3350EUHF#PBF-ND, JLCPCB→C580711
   - TPS25751DREFR: DigiKey→296-TPS25751DREFRCT-ND, JLCPCB→C30169739
   - TPS2372-4RGWR: JLCPCB→C470955
   - TPS23730RMTR: JLCPCB→C3189530
   - TPD4E05U06DRYR: **INVALID MPN** — needs replacement ESD part selection
   - TPD2E2U06DRLR: JLCPCB→C1972959
   - TPD1E10B06: specific variant = **TPD1E10B06DYARQ1** SOD-523, DigiKey→296-TPD1E10B06DYARQ1CT-ND, Mouser→595-TPD1E10B06DYARQ1, JLCPCB→C3013901
   - FT232HL-REEL: DigiKey→768-1101-1-ND, JLCPCB→C51997 (was C123467)
   - EPM570T100I5N: DigiKey→544-2281-ND, JLCPCB→C27319
   - FDC2114RGER: **wrong MPN** — should be **FDC2114RGHR**, DigiKey→FDC2114RGHR-ND (MOQ 4500), Mouser→595-FDC2114RGHR (MOQ 4500), JLCPCB→C2652079 (MOQ 2)
   - CSD17483F4T: DigiKey→296-37781-1-ND, JLCPCB→C2871105
   - BSS138 (onsemi): DigiKey→BSS138CT-ND, Mouser→512-BSS138, JLCPCB→C255592
   - BAT54 (Diotec): DigiKey→4878-BAT54CT-ND, Mouser→637-BAT54, JLCPCB→C25835522
   - User downloaded datasheets #1–#27; asked for datasheet links to point to local PDFs in `design/Datasheets/`
4. **All corrections applied** (commit `70689cf`):
   - Global `FDC2114RGER→FDC2114RGHR` rename across 9 files
   - All PN corrections applied in Consolidated_BOM.md, Power_Module/Design_Spec.md, JTAG_Daughterboard/Design_Spec.md, Controller/Design_Spec.md, Stator/Design_Spec.md, Rotor/Design_Spec.md
   - Section 11 Datasheet Links completely replaced with local PDF paths
   - TPD4E05U06 marked INVALID everywhere; TPD1E10B06DYARQ1 updated with SOD-523 package
   - markdownlint clean (only 2 pre-existing acceptable MD013 warnings remain)
</history>

<work_done>
Files modified in this session (commit `70689cf`):
- `design/Electronics/Consolidated_BOM.md` — FDC2114 rename; all PN corrections; §11 rebuilt with local PDF links; EPM570 PNs; CSD17483F4T, FT232H, TPD PNs; TPD4E05U06 marked invalid
- `design/Electronics/Power_Module/Design_Spec.md` — D1 → TPD1E10B06DYARQ1 SOD-523; D3/D4/D5 → TBD invalid MPN
- `design/Electronics/Controller/Design_Spec.md` — U4 → TBD invalid MPN
- `design/Electronics/JTAG_Daughterboard/Design_Spec.md` — U1 FT232H PNs corrected
- `design/Electronics/Stator/Design_Spec.md` — U1 EPM570 PNs updated
- `design/Electronics/Rotor/Design_Spec.md` — U1 EPM570 PNs; U2/U3/U4 FDC2114RGHR PNs
- `design/Electronics/Rotor/Board_Layout.md` — FDC2114 rename
- `design/Electronics/Rotor/Rotor_26_Char_Design.md` — FDC2114 rename
- `design/Electronics/Rotor/Rotor_64_Char_Design.md` — FDC2114 rename
- `design/Electronics/Power_Budgets.md` — FDC2114 rename
- `design/Electronics/Boards_Overview.md` — FDC2114 rename
- `design/Design_Log.md` — FDC2114 rename
- `design/Standards/Certification_Evidence.md` — FDC2114 rename
- `design/Mechanical/Rotor/Design_Spec.md` — FDC2114 rename
- `design/Datasheets/` — 23 PDF files now tracked in git

Previously completed (commit `7e165cb` — revert agent):
- eFuse TPS259807→TPS259804ONRGER in PM/Design_Spec, Consolidated_BOM, Certification_Evidence, Design_Log
- Reflector R1 0603 package restored in Reflector/Design_Spec and Consolidated_BOM

Commit trail:
| Hash | Description |
|------|-------------|
| `4f38141` | Checkpoint 019 — split rotor, mechanical specs |
| `5fd19a8`–`eb260d5` | R1–R7 review fixes |
| `b6ad5ca` | Checkpoint 020 |
| `7e165cb` | Revert eFuse/R1 corrections |
| `70689cf` | PN corrections, FDC2114RGHR, local datasheets |
</work_done>

<technical_details>
**Critical part number corrections confirmed:**
- FDC2114RGER was wrong → **FDC2114RGHR** is the correct TI MPN. Datasheet: `fdc2112-datasheet.pdf` (covers both FDC2112 and FDC2114 family). ⚠️ MOQ 4500 at Mouser/DigiKey — JLCPCB C2652079 has MOQ 2, making it the preferred procurement route.
- TPD4E05U06DRYR is **not a valid TI part number**. All 4× ESD array positions (PM D3/D4/D5 + CTL U4) need replacement part selection before schematic capture.
- TPD1E10B06DYARQ1 is the specific variant chosen (SOD-523 package, AEC-Q100 automotive grade).
- TPS259804ONRGER (silicon-fixed 16.9V OVLO) is correct. TPS259807 = NO OVLO variant and must never be used.

**FDC2114RGHR procurement warning:**
- MOQ 4500 at Mouser and DigiKey for the full design (60–90 ICs required for 30 rotors at 2–3 per rotor)
- JLCPCB C2652079 has MOQ 2 — recommended for PCB assembly orders
- For prototyping, note that quantities fit within JLCPCB's global sourcing if using their SMT service

**Datasheet folder:**
- `design/Datasheets/` now contains 23 PDFs tracked in git
- All section 11 links in Consolidated_BOM.md use relative paths: `../Datasheets/<filename>.pdf`
- `fdc2112-datasheet.pdf` covers both FDC2112 and FDC2114 family
- `Intel_max2_cpld-handbook.pdf` covers both EPM240 and EPM570

**Stale values — MUST NEVER reappear:**
- FDC2114RGER (wrong MPN for capacitive sensor — use FDC2114RGHR)
- TPS259807ONRGER (wrong eFuse variant — use TPS259804ONRGER)
- TPD4E05U06DRYR (invalid MPN — awaiting replacement)
- 768-1014-ND / C123467 for FT232H (wrong PNs — use 768-1101-1-ND / C51997)

**markdownlint status:** Clean except 2 pre-existing acceptable MD013 warnings:
- `design/Guides/User_Manual.md:134` (line too long, acceptable)
- `design/Standards/Global_Routing_Spec.md:72` (line too long, acceptable)
</technical_details>

<important_files>
- `design/Electronics/Consolidated_BOM.md`
  - Master BOM for all boards; section 11 rebuilt with local PDF datasheet links
  - All supplier PNs corrected; FDC2114RGHR throughout; TPD4E05U06 marked invalid
  - Lines 29–31: FDC2114RGHR component usage summary rows
  - Line ~285: U1 eFuse TPS259804ONRGER (confirmed correct)
  - Section 11 (~line 335): complete datasheet reference table with local PDF paths
- `design/Electronics/Power_Module/Design_Spec.md`
  - Contains eFuse, LDO, buck, supercap, ESD circuits
  - D1: now TPD1E10B06DYARQ1 SOD-523; D3/D4/D5: TBD invalid MPN
  - U1 eFuse: TPS259804ONRGER confirmed correct
- `design/Electronics/Rotor/Design_Spec.md`
  - FDC2114RGHR U2/U3/U4 BOM rows updated with correct PNs and MOQ warnings
  - U1 EPM570T100I5N: DigiKey 544-2281-ND, JLCPCB C27319
- `design/Datasheets/`
  - 23 PDF datasheets now tracked in git and linked from Consolidated_BOM.md §11
  - Key files: TPS25980, ltc3350, fdc2112 (covers FDC2114RGHR), Intel_max2_cpld-handbook
- `design/Electronics/Controller/Design_Spec.md`
  - U4 ESD: TBD (TPD4E05U06DRYR invalid)
- `design/Design_Log.md`
  - FDC2114RGHR rename in DEC-027 description
</important_files>

<next_steps>
**Active open item — critical:**
- **TPD4E05U06DRYR is INVALID** — need to select replacement 4-channel ESD array for:
  - PM D3 (USB-C entry, 4 lines)
  - PM D4 (RJ45 MDI0/MDI1, 4 lines)
  - PM D5 (RJ45 MDI2/MDI3, 4 lines)
  - CTL U4 (USB 3.0 + HDMI ESD, 4 lines)
  - Suggested search: TI TPD4E004DRYR, Nexperia PRTR5V0U4, or similar 4-ch ESD array compatible with USB 3.0 / HDMI / GbE MDI
  - User to select; then update PM/Design_Spec, Controller/Design_Spec, Consolidated_BOM

**User is continuing parts verification (#28 onwards — see reprinted list below)**

**Other pending items (lower priority):**
- `kicad-setup-docs` todo — KiCad project setup documentation
- OWI-019: Relocate STGC_Generator.py to `design/Electronics/Rotor/`
- OWI-020: GUI App — DEC-027/FR-ROT-09 cross-reference
- OWI-021: Complete 6 Mechanical stub files (Encoder, Stator, Reflector, Extension, JDB, PM)
- Tecate SCMT32C156PRBA0 (22F/2.7V supercap) supplier PNs still TBD
- Würth 61201221721 DigiKey PN still TBD
- CTS 219-6LPST DigiKey/JLCPCB PNs still TBD
- Marquardt 1800 series power switch — open item pending mechanical design
- User manual review before final design sign-off
- Checkpoint to be created after user completes parts verification
</next_steps>

---

Now here is the list reprinted from **#28 onwards** with corrected #1–#27 datasheet links for reference at the top, then continuing from Passive Components:

---
### Updated #1–#27 ICs & Active Devices (datasheet links now local PDFs)
| # | MPN | Description | Board(s) | Mouser | DigiKey | JLCPCB | Datasheet |
|---|-----|-------------|----------|--------|---------|--------|-----------|
| 1 | TPS259804ONRGER | eFuse 16.9V silicon-fixed OVLO, VQFN-24 | PM U1 | 595-TPS259804ONRGER | 296-TPS259804ONRGERCT-ND | C2878936 | [TPS25980-datasheet.pdf](design/Datasheets/TPS25980-datasheet.pdf) |
| 2 | LMQ61460AFSQRJRRQ1 | 6A Sync Buck AEC-Q100, VQFN-HR RJR 14-pin | PM U2A/B | 595-Q61460AFSQRJRRQ1 | 296-LMQ61460AFSQRJRRQ1CT-ND | C1518767 | [lmq61460-q1-datasheet.pdf](design/Datasheets/lmq61460-q1-datasheet.pdf) |
| 3 | LTC3350EUHF#PBF | Supercap Manager/Charger/Backup, QFN-38 | PM U3 | 584-LTC3350EUHF#PBF | 505-LTC3350EUHF#PBF-ND | C580711 | [ltc3350-datasheet.pdf](design/Datasheets/ltc3350-datasheet.pdf) |
| 4 | TPS25751DREFR | USB PD 3.1 DRP Controller, WQFN-38 ⚠️ footprint change | PM U4 | 595-TPS25751DREFR | 296-TPS25751DREFRCT-ND | C30169739 | [tps25751-datasheet.pdf](design/Datasheets/tps25751-datasheet.pdf) |
| 5 | STUSB4500LQTR | USB-C Sink PD Controller, QFN-24 | PM U5 | 511-STUSB4500LQTR | 497-STUSB4500LQCT-ND | C506650 | [stusb4500l-datasheet.pdf](design/Datasheets/stusb4500l-datasheet.pdf) |
| 6 | LM74700QDBVRQ1 | Ideal-Diode OR Controller, SOT-23-6 | PM U6 ×3 | 595-LM74700QDBVRQ1 | 296-LM74700QDBVRQ1CT-ND | C2941042 | [lm74700-q1-datasheet.pdf](design/Datasheets/lm74700-q1-datasheet.pdf) |
| 7 | TPS75733KTTRG3 | 3.3V 3A LDO, TO-263 KTT 5-pin | PM U7 | 595-TPS75733KTTRG3 | 296-50559-1-ND | C3749924 | [tps757-datasheet.pdf](design/Datasheets/tps757-datasheet.pdf) |
| 8 | MCP121T-450E/LB | 4.50V Voltage Supervisor, SC70-3 | PM U8 | 579-MCP121T-450E/LB | MCP121T-450E/LBCT-ND | C52146050 | [MCP121-datasheet.pdf](design/Datasheets/MCP121-datasheet.pdf) |
| 9 | TPS2372-4RGWR | PoE PD Interface 802.3bt Type 4, VQFN-20 | PM U9 | 595-TPS2372-4RGWR | 296-52795-1-ND | C470955 | [tps2372-datasheet.pdf](design/Datasheets/tps2372-datasheet.pdf) |
| 10 | TPS23730RMTR | PoE ACF DC-DC Controller, WQFN-20 | PM U10 | 595-TPS23730RMTR | 296-TPS23730RMCT-ND | C3189530 | [tps23730-datasheet.pdf](design/Datasheets/tps23730-datasheet.pdf) |
| 11 | MIC1555YM5-TR | CMOS Timer SOT-23-5 (×2: U11 LED + U15 monostable) | PM U11/U15 | 579-MIC1555YM5TR | MIC1555YM5-TRCT-ND | C431119 | [MIC1555-datasheet.pdf](design/Datasheets/MIC1555-datasheet.pdf) |
| 12 | INA219AIDR | Zero-Drift Power Monitor, SOIC-8 | PM U12 (0x40); STA U2 (0x45) | 595-INA219AIDR | 296-23978-1-ND | C138706 | [INA219-datasheet.pdf](design/Datasheets/INA219-datasheet.pdf) |
| 13 | SN74LVC1G14DBVRQ1 | Single Schmitt-Trigger Inverter, SOT-23-5 | PM U13/U14 | 595-SN74LVC1G14DBVRQ1 | 296-SN74LVC1G14DBVRQ1CT-ND | C914967 | [sn74lvc1g14-q1-datasheet.pdf](design/Datasheets/sn74lvc1g14-q1-datasheet.pdf) |
| 14 | TPS2065CDBVR | USB Power Distribution Switch 1.6A, SOT-23-5 | CTL U2 | 595-TPS2065CDBVR | 296-TPS2065CDBVRCT-ND | C123460 | [tps2065c-datasheet.pdf](design/Datasheets/tps2065c-datasheet.pdf) |
| 15 | AP2331W-7 | HDMI Current Limiter 50mA, SOT-23-5 | CTL U3 | 621-AP2331W-7 | AP2331W-7DICT-ND | C123461 | [AP2331-datasheet.pdf](design/Datasheets/AP2331-datasheet.pdf) |
| 16 | ~~TPD4E05U06DRYR~~ | ⚠️ **INVALID MPN — part selection required** for 4-ch ESD (PM D3/D4/D5 + CTL U4) | PM ×3; CTL ×1 | — | — | — | TBD |
| 17 | TPD2E2U06DRLR | Dual 5.5V SMBus ESD, SOT-553 | PM D2 | 595-TPD2E2U06DRLR | 296-38361-1-ND | C1972959 | [tpd2e2u06-datasheet.pdf](design/Datasheets/tpd2e2u06-datasheet.pdf) |
| 18 | TPD1E10B06DYARQ1 | Single-ch 10V TVS ESD, SOD-523 | PM D1 | 595-TPD1E10B06DYARQ1 | 296-TPD1E10B06DYARQ1CT-ND | C3013901 | [tpd1e10b06-q1-datasheet.pdf](design/Datasheets/tpd1e10b06-q1-datasheet.pdf) |
| 19 | SN74LVC2G125DCUR | Dual 3-State Buffer, VSSOP-8 | EXT U1; JDB U5 | 595-SN74LVC2G125DCUR | 296-SN74LVC2G125DCURCT-ND | C21404 | [sn74lvc2g125-datasheet.pdf](design/Datasheets/sn74lvc2g125-datasheet.pdf) |
| 20 | FT232HL-REEL | USB 2.0 MPSSE Bridge, QFN-56 | JDB U1 | 895-FT232HL-REEL | 768-1101-1-ND | C51997 | [FT232H-datasheet.pdf](design/Datasheets/FT232H-datasheet.pdf) |
| 21 | EPM240T100I5N | Intel MAX II CPLD 240 LE TQFP-100 (industrial) | ENC ×2/board (6 total) | 989-EPM240T100I5N | 544-2276-ND | C40067 | [Intel_max2_cpld-handbook.pdf](design/Datasheets/Intel_max2_cpld-handbook.pdf) |
| 22 | EPM570T100I5N | Intel MAX II CPLD 570 LE TQFP-100 (industrial) | STA ×1; ROT ×1/board (31 total) | 989-EPM570T100I5N | 544-2281-ND | C27319 | [Intel_max2_cpld-handbook.pdf](design/Datasheets/Intel_max2_cpld-handbook.pdf) |
| 23 | FDC2114RGHR | 4-ch Capacitive Sensor IC, 16-VQFN ⚠️ MOQ 4500 at distributors | ROT U2/U3/U4 (60–90 total) | 595-FDC2114RGHR | FDC2114RGHR-ND | C2652079 (MOQ 2) | [fdc2112-datasheet.pdf](design/Datasheets/fdc2112-datasheet.pdf) |
| 24 | CM5 (SC1180) | RPi Compute Module 5 — min 8GB/4GB eMMC | CTL U1 | — (RPi distributors) | — | — | [RPi-cm5-datasheet.pdf](design/Datasheets/RPi-cm5-datasheet.pdf) |
| 25 | CSD17483F4T | N-ch MOSFET 30V/10A OR-ing, SON-8 | PM Q1/Q2/Q3 | 595-CSD17483F4T | 296-37781-1-ND | C2871105 | [csd17483f4-datasheet.pdf](design/Datasheets/csd17483f4-datasheet.pdf) |
| 26 | BSS138 (onsemi) | N-ch Logic MOSFET 50V, SOT-23 | PM Q4/Q5 | 512-BSS138 | BSS138CT-ND | C255592 | [BSS138-onsemi-datasheet.pdf](design/Datasheets/BSS138-onsemi-datasheet.pdf) |
| 27 | BAT54 (Diotec) | Schottky Diode, SOT-23 | PM ×2; CTL D1 (3 total) | 637-BAT54 | 4878-BAT54CT-ND | C25835522 | [bat54-diotec-datasheet.pdf](design/Datasheets/bat54-diotec-datasheet.pdf) |

---
### Passive Components (continuing from #28)
| # | MPN | Description | Board(s) | Mouser | DigiKey | JLCPCB |
|---|-----|-------------|----------|--------|---------|--------|
| 28 | Tecate SCMT32C156PRBA0 | 22F / 2.7V Supercap SMD (×6 in 2S3P) | PM C_SC1–6 | **TBD** | **TBD** | **TBD** |
| 29 | Bourns CSS2H-2512R-R010ELF | 10mΩ ±1% 2512 Kelvin shunt | PM R12/R23; STA R1 (3 total) | 652-CSS2H-2512R-R010ELF | CSS2H-2512R-R010ELF-ND | — |
| 30 | Samsung CL05B104KB5NNNC | 100nF X7R 50V 0402 decoupling | All boards (~509 total) | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| 31 | Samsung CL31B106KBHNNNE | 10µF X7R 50V 1206 bulk decoupling | CTL/STA/ENC/ROT/REF/EXT | 187-CL31B106KBHNNNE | 1276-6767-1-ND | C89632 |
| 32 | Samsung CL32B226KAJNNNE | 22µF X7R 25V 1210 bulk cap | PM | 187-CL32B226KAJNNNE | 1276-3392-1-ND | C309062 |
| 33 | Kemet C0805C105K5RACTU | 1µF X7R 50V 0805 | PM C2/C5/C23 | 80-C0805C105K5R | — | — |
| 34 | Kemet C1206C106K3RACTU | 10µF X7R 25V 1206 LDO input | PM C13 | 80-C1206C106K3R | — | — |
| 35 | Samsung CL10B106KA8NNNC | 10µF X7R 16V 0603 monostable cap | PM C32 | 187-CL10B106KA8NNNC | — | — |
| 36 | Samsung CL10B223KB8WPNC | 22nF X7R 25V 0603 SYNC delay | PM C29 | 187-CL10B223KB8WPNC | — | — |
| 37 | Samsung CL05B103KB5NNNC | 10nF X7R 50V 0402 soft-start | PM C24 | 187-CL05B103KB5NNNC | — | — |
| 38 | Kemet C0402C101K3RACAUTO | 100pF X7R 25V 0402 SYNC filter | PM C28 | 80-C0402C101K3RAUTO | — | — |
| 39 | Kemet C0402C103J1RACAUTO | 10nF 100V X7R 0402 Bob Smith | PM C25 | 80-C0402C103J1RAUTO | 399-C0402C103J1RACAUTOCT-ND | C19862706 |
| 40 | Abracon ABM8-12.000MHz-B2-T | 12MHz 20pF ±20ppm SMD3225 crystal | JDB Y1 | 815-ABM8-12.000MHZ-B2-T | 535-9977-1-ND | C9002 |
| 41 | Würth 150060VS75000 | Green SMD LED Vf≈2.0V@10mA, 0402 | ENC D1/D2 (6 total) | 710-150060VS75000 | 732-5015-1-ND | C2286 |
| 42 | Laird HI1206P121R-10 | Ferrite bead 120Ω@100MHz 4.0A, 1206 | STA L1–L4 (4 total) | 875-HI1206P121R-10 | 240-2410-1-ND | C2442103 |
| 43 | Bourns AC72ABD | 72°C SMD Thermal Cutoff (TCO) | PM F1 | Search bourns.com AC72 | — | — |
| 44 | ERA-3ARB2872V | 28.7kΩ 0.1% thin-film 0603 (LTC3350 BACKUP R_TOP) | PM R14 | 667-ERA-3ARB2872V | P28.7KBYCT-ND | — |
| 45 | ERA-3ARB1002V | 10.0kΩ 0.1% thin-film 0603 (LTC3350 BACKUP R_BOT) | PM R15 | 667-ERA-3ARB1002V | P10.0KBYCT-ND | — |
| 46 | ERJ-3EKF2323V | 232kΩ 1% thick-film 0603 (eFuse UVLO R1) | PM R1 | 667-ERJ-3EKF2323V | P232KHCT-ND | C403086 |
| 47 | ERJ-3EKF2872V | 28.7kΩ 1% thick-film 0603 (eFuse UVLO R2) | PM R2 | 667-ERJ-3EKF2872V | P28.7KHCT-ND | C403135 |
| 48 | ERJ-3EKF2100V | 210Ω 1% thick-film 0603 (eFuse ILIM R3) | PM R3 | 667-ERJ-3EKF2100V | P210HCT-ND | C403064 |
| 49 | ERJ-3EKF8662V | 86.6kΩ 1% thick-film 0603 (SYNC F_SET) | PM | 667-ERJ-3EKF8662V | — | — |
| 50 | ERJ-2RKF8202X | 82.0kΩ 1% thick-film 0402 (SYNC R_DLY) | PM | 667-ERJ-2RKF8202X | — | — |
| 51 | ERJ-3EKF2743V | 274kΩ 1% thick-film 0603 (MIC1555 U15 R28) | PM | 667-ERJ-3EKF2743V | — | — |
| 52 | ERJ-3EKF7153V | 715kΩ 1% thick-film 0603 (MIC1555 U11 R_B) | PM | 667-ERJ-3EKF7153V | — | — |
| 53 | ERJ-3EKF1213V | 121kΩ 1% thick-film 0603 (PoE RMPS R13) | PM | 667-ERJ-3EKF1213V | — | — |
| 54 | ERJ-3EKF3010V | 301Ω 1% thick-film 0603 (LTC3350 R_ICHARGE) | PM | 667-ERJ-3EKF3010V | — | — |
| 55 | ERJ-3EKF4701V | 4.7kΩ 1% thick-film 0603 (I²C pull-ups) | PM | 667-ERJ-3EKF4701V | — | — |
| 56 | ERJ-3EKF3300V | 330Ω 1% thick-film 0603 (Ethernet LED) | PM | 667-ERJ-3EKF3300V | — | C25803 |
| 57 | ERJ-3EKF1002V | 10kΩ 1% thick-film 0603 (pull-ups/downs) | PM/CTL/STA | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| 58 | ERJ-3EKF75R0V | 75Ω 1% thick-film 0603 (JTAG series, Stator) | STA R7–R15 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| 59 | ERJ-3EKF2200V | 22Ω 1% thick-film 0603 (JTAG EOC damping) | REF R1 | 667-ERJ-3EKF2200V | P22.0BYCT-ND | — |
| 60 | ERJ-3EKF1000V | 100Ω 1% thick-film 0603 (differential term) | CTL R2 | 667-ERJ-3EKF1000V | P100BYCT-ND | C25806 |
| 61 | ERJ-3GEY0R00V | 0Ω 0603 bond/isolating resistor | EXT R1/R2 | 667-ERJ-3GEY0R00V | P0.0BYCT-ND | C25807 |
| 62 | ERJ-2RKF1002X | 10kΩ 1% thick-film 0402 (JTAG pull-ups/downs) | ENC/ROT/JDB | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| 63 | ERJ-2RKF75R0X | 75Ω 1% thick-film 0402 (JTAG series) | ENC R8; ROT R1 | 667-ERJ-2RKF75R0X | P75.0LCT-ND | C413061 |
| 64 | ERJ-2RKF33R0X | 33Ω 1% thick-film 0402 (JTAG series) | ENC R7; JDB R2/R6/R7/R8 | 667-ERJ-2RKF33R0X | P33.0LBCT-ND | C25808 |
| 65 | ERJ-2RKF3300X | 330Ω 1% thick-film 0402 (LED current limit) | ENC R1/R2 | 667-ERJ-2RKF3300X | P330LBCT-ND | C105872 |
| 66 | Kemet C0402C330J5GAUTO | 33pF C0G/NP0 0402 crystal load (**sole C0G exception in design**) | JDB C10/C11 | 80-C0402C330J5GAUTO | 399-12979-1-ND | C2169327 |

---
### Connectors (continuing)
| # | MPN | Description | Board(s) | Mouser | DigiKey | JLCPCB |
|---|-----|-------------|----------|--------|---------|--------|
| 67 | ERM8-040-05.0-S-DV-K-TR | 80-pin BtB Male 0.8mm (Link-Alpha) | PM J1 | 200-ERM8040050SDVKTR | SAM8621CT-ND | — |
| 68 | ERF8-040-05.0-S-DV-K-TR | 80-pin BtB Female 0.8mm (Link-Alpha) | CTL J1 | 200-ERF8040050SDVKTR | SAM8621CT-ND | C3640808 |
| 69 | ERM8-020-05.0-S-DV-K-TR | 40-pin BtB Male 0.8mm (Link-Beta) | STA J8 | 200-ERM8020050SDVKTR | SAM8611CT-ND | C138400 |
| 70 | ERF8-020-05.0-S-DV-K-TR | 40-pin BtB Female 0.8mm (Link-Beta) | CTL J2 | 200-ERF8020050SDVKTR | SAM8619CT-ND | C6034565 |
| 71 | ERM8-005-05.0-S-DV-K-TR | 10-pin BtB Male 0.8mm | ROT J1/J2; REF J1/J2; EXT J1/J2 (64 total) | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 |
| 72 | ERF8-005-05.0-S-DV-K-TR | 10-pin BtB Female 0.8mm | STA J1/J2 per slot; ROT J4/J5; EXT J4/J5 (64 total) | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 |
| 73 | ERM8-010-05.0-S-DV-K-TR | 20-pin BtB Male 0.8mm (ENC data in) | ROT J3; REF J3; EXT J3 (32 total) | 200-ERM8010050SDVKTR | SAM8610CT-ND | C374877 |
| 74 | ERF8-010-05.0-S-DV-K-TR | 20-pin BtB Female 0.8mm (ENC data out) | STA J3 per slot; ROT J6; EXT J6 (32 total) | 200-ERF8010050SDVKTR | SAM8618CT-ND | C3646170 |
| 75 | Würth 61201221721 | 2×11 22-pin keyed IDC box header 2.54mm (J_INT, hand-assembled post-SMT) | ROT ×2 per assembly (60 total) | 710-61201221721 | **TBD** | N/A |
| 76 | Molex 22-23-2261 | 26-pin 2×13 shrouded header 2.54mm | STA J4/J5/J6; ENC J2 (6 total) | 538-22-23-2261 | WM2913-ND | N/A |
| 77 | Molex 22-23-2161 | 16-pin 2×8 shrouded header 2.54mm | STA J7; REF J4; EXT J7/J8 (4 total) | 538-22-23-2161 | WM2907-ND | N/A |
| 78 | Amphenol 10164227-1004A1RLF | CM5 100-pin SO-DIMM socket 4.0mm | CTL J_CM5_A/B | 649-101642271004RLF | 609-10164227-1004A1RLFCT-ND | C7435219 |
| 79 | Molex 48406-0003 | USB 3.0 Type-A Dual-Stack THT | CTL J3 | 538-0484060003 | WM1394-ND | C123458 |
| 80 | TE 2007435-1 | HDMI Type-A Full-Size THT | CTL J4 | 571-2007435-1 | A125057-ND | C123459 |
| 81 | GCT USB4135-GF-A | USB-C SMT Receptacle 5A 6-pos | PM J4 | 640-USB4135-GF-A | 2073-USB4135-GF-A-ND | — |
| 82 | Würth 7499111121A | GbE RJ45 MagJack with LEDs THT | PM J2 | 710-7499111121A | 1297-1070-5-ND | — |
| 83 | Molex 43650-0519 | Micro-Fit 3.0 5-pin Vertical THT (Battery) | PM J3 | 538-43650-0519 | WM14587-ND | C563849 |
| 84 | JST SM04B-SRSS-TB(LF)(SN) | 4-pin 1.0mm Fan Header SMT | CTL J_FAN | 538-SM04B-SRSS-TB | — | C160390 |
| 85 | 1×5 2.54mm Female IDC | JDB INPUT header | JDB J1 | — | — | C50950 |
| 86 | 1×10 2.54mm Female IDC | JDB JTAG OUTPUT header | JDB J2 | — | — | C2337 |

---
### Electromechanical & Hardware
| # | MPN | Description | Board(s) | Mouser | DigiKey | JLCPCB |
|---|-----|-------------|----------|--------|---------|--------|
| 87 | Würth WE-CMBNC 7448031002 | 2mH 10A Nanocrystalline EMI CMC THT | PM L1/L2 | 710-7448031002 | 732-5584-ND | C1519839 |
| 88 | Bourns SRP1265A-100M | 10µH 15.5A DM Inductor SMT | PM L3 | 652-SRP1265A-100M | — | — |
| 89 | Coilcraft POE600F-12LD | 60W ACF PoE Isolation Transformer | PM T2 | (order direct from Coilcraft) | — | — |
| 90 | Keystone 1285-ST | 6.35mm PCB blade terminal THT (Encoder spade rows) | ENC BT1–128 (384 total) | 534-1285-ST | 36-1285-ST-ND | C5370868 |
| 91 | Keystone 3034 | CR2032 THT horizontal coin cell holder | CTL BT1 | 534-3034 | 36-3034-ND | C70377 |
| 92 | Renata CR2032 | 3V Coin Cell (installed at commissioning) | CTL | 614-CR2032 | P189-ND | — |
| 93 | Würth 9774040151R | M2.5×4.0mm SMT Brass Standoff (CM5 mount) | CTL MH1–MH4 | 710-9774040151R | 732-7089-1-ND | C5182034 |
| 94 | CTS 219-4LPST | 4-position DIP switch 2.54mm THT | STA SW1 | 774-219-4LPST | CT2064-ND | C128947 |
| 95 | CTS 219-6LPST | 6-position DIP switch 2.54mm THT | STA SW2; ROT SW1/SW2/SW3 | 774-219-6LPST | **TBD** | **TBD** |
| 96 | Marquardt 1800 series | Main Power Toggle + RGB LED rocker | PM SW1 | **Open item — TBD** | **TBD** | — |
| 97 | ALPS SKRPACE010 | Tactile SMT Reset Switch | PM SW2 | 688-SKRPACE010 | 688-SKRPACE010-ND | C115337 |
| 98 | 6.35mm Mono Switched Jack | Panel-mount plugboard jack (already purchased) | ENC J1 ×64 (192 total) | — (eBay: SaiBuy.Ltd item 334364197440) | — | — |
| 99 | DPDT 6-pin Keyboard Switch | Momentary keyboard switch (already purchased) | ENC SW1–64 (192 total) | — (eBay: gadgetkingdom) | — | — |

---
### ⚠️ Outstanding Items — Action Required
| # | Item | Status | Action |
|---|------|--------|--------|
| A | **~~TPD4E05U06DRYR~~** (4×ESD positions: PM D3/D4/D5, CTL U4) | **INVALID MPN** | Select replacement 4-ch ESD array (e.g. TI TPD4E004DRYR, Nexperia PRTR5V0U4T) |
| B | **Tecate SCMT32C156PRBA0** (supercap) | Mouser/DigiKey/JLCPCB PNs all **TBD** | Verify availability and obtain catalog PNs |
| C | **Würth 61201221721** (J_INT IDC) | DigiKey PN **TBD** | Confirm DigiKey PN |
| D | **CTS 219-6LPST** (6-pos DIP) | DigiKey/JLCPCB **TBD** | Confirm PNs |
| E | **TPS25751DREFR** footprint | ⚠️ Package QFN-28→WQFN-38 | Update schematic symbol and PCB footprint |
