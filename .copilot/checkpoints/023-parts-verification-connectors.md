<overview>
The session is focused on completing a master parts list verification for the Enigma-NG hardware project — a custom Enigma cipher machine with multiple PCB boards. The user is manually verifying every component MPN and supplier part number (Mouser/DigiKey/JLCPCB) against actual distributor listings, providing corrections, and the agent applies all changes to the design documents. The goal is to ensure the complete BOM is accurate before declaring the design complete and proceeding to KiCad schematic capture.
</overview>

<history>
1. **Session resumed from checkpoint 022** — user completed parts verification #1–#27 (ICs/active devices) in the prior session. All corrections were applied in commit `70689cf`: FDC2114RGER→FDC2114RGHR globally, TPD1E10B06→TPD1E10B06DYARQ1 SOD-523, TPD4E05U06DRYR marked invalid, LTC3350/TPS25751/FT232H/EPM570 PNs corrected, Consolidated_BOM §11 datasheet links updated to local PDFs. Reprinted list from #28 onward was provided.
2. **User provided connector PN corrections (#67–#86):**
   - ERM8-040: DigiKey SAM8613CT-ND (was wrongly SAM8621CT-ND), JLCPCB C5358550
   - ERF8-040: confirmed SAM8621CT-ND, C3640808
   - Molex 48406-0003: DigiKey WM10420-ND, JLCPCB C565298
   - TE 2007435-1: DigiKey A141617-ND, JLCPCB C195051
   - GCT USB4135-GF-A: DigiKey 2073-USB4135-GF-ACT-ND, JLCPCB C5438410
   - Würth 7499111121A: JLCPCB C5523983
   - JST SM04B-SRSS-TB: DigiKey 455-SM04B-SRSS-TBCT-ND, Mouser 306-SM04BSRSSTBLFSN, JLCPCB C160404
   - Würth 61201221721: **MPN does not exist** — flagged for redesign
   - Molex 22-23-2261 and 22-23-2161: **wrong parts for description** — flagged for redesign
   - 1×5 and 1×10 2.54mm Female IDC (JDB J1/J2): **no suitable part found** — flagged for redesign
   - User also added new datasheets: ERM8 series, ERF8 series, Amphenol CM5 socket, Molex 48406, TE 2007435-1, GCT USB4135, Würth 7499111121A
   - Agent applied all changes across 9 files (commit `75402d4`), §11 expanded with 7 new datasheet links
3. **TPS25751DREFR package confirmed WQFN-38 (review item I):**
   - User confirmed package is WQFN-38 — already correct in docs
   - Agent fixed stale DigiKey PN `TPS25751DREFR-ND` → `296-TPS25751DREFRCT-ND` in PM/Design_Spec.md and Design_Log.md
   - Lint error introduced and fixed (line too long); commit `953e033`
4. **Footprint warning language removed (review item I clarified):**
   - User clarified KiCad projects not started yet — footprint warnings premature
   - All ⚠️ "schematic symbol and PCB footprint update required" language removed from 4 locations
   - Package retained as informational note only; commit `b3e1800`
5. **FDC2114RGHR MOQ (review item K) closed:**
   - User confirmed JLCPCB assembly will be used — MOQ 4500 at Mouser/DigiKey is irrelevant
   - No doc changes needed; item closed
6. **TPD4E05U06 variant selected (review item A):**
   - User provided: MPN = **TPD4E05U06QDQARQ1**, DigiKey = 296-40696-1-ND, Mouser = 595-PD4E05U06QDQARQ1, JLCPCB = C81353
   - Updated PM D3/D4/D5 and CTL U4 BOM rows, Consolidated_BOM summary row, §11 datasheet row, Design_Log INC-22
   - Agent noted Mouser PN appeared to be missing leading "T"; user confirmed it is correct as-is (copied directly from Mouser)
   - Commit `1d5e969`
7. **Supercap replacement research (review item B):**
   - Tecate SCMT32C156PRBA0 confirmed as non-existent/unavailable
   - Required specs established from design docs: **22F, 2.7V per cell, SMD, 6 cells in 2S3P**, LTC3350-managed, ESR as low as possible, −40°C to +65°C operating range, footprint ~32mm diameter can SMD
   - User asked about **Vishay MAL222551017E3** as a candidate
   - Web lookups attempted — Octopart confirms the part exists, stocked at Newark (SKU 78K8917) with ~1,382 units; Mouser/Vishay direct pages inaccessible due to 403/404 errors
   - Full spec details not yet retrieved — session compaction requested before resolution
</history>

<work_done>
Files modified (this session):

- `design/Electronics/Consolidated_BOM.md` — connector PNs corrected; 5 connectors flagged ⚠️; §11 expanded with 7 connector datasheet links; TPD4E05U06QDQARQ1 selected; TPS25751 footprint warnings removed
- `design/Electronics/Power_Module/Design_Spec.md` — D3/D4/D5 BOM rows updated to TPD4E05U06QDQARQ1; TPS25751 package note cleaned up; DigiKey PN corrected
- `design/Electronics/Controller/Design_Spec.md` — U4 BOM row updated to TPD4E05U06QDQARQ1; connector J3/J4 PNs corrected
- `design/Electronics/JTAG_Daughterboard/Design_Spec.md` — J1/J2 IDC headers flagged ⚠️
- `design/Electronics/Rotor/Design_Spec.md` — J_INT (Würth 61201221721) flagged ⚠️
- `design/Electronics/Stator/Design_Spec.md` — J4-J6 (22-23-2261) and J7 (22-23-2161) flagged ⚠️
- `design/Electronics/Encoder/Design_Spec.md` — J2 (22-23-2261) flagged ⚠️
- `design/Electronics/Extension/Design_Spec.md` — J7/J8 (22-23-2161) flagged ⚠️
- `design/Electronics/Reflector/Design_Spec.md` — J4 (22-23-2161) flagged ⚠️
- `design/Design_Log.md` — INC-22 updated with TPD4E05U06QDQARQ1; TPS25751 PN corrected; footprint warning removed
- `design/Datasheets/` — 7 new PDFs tracked: erm8, erf8, Amphenol, Molex-48406, TE-2007435-1, usb4135, Wurth-7499111121A

Commit trail this session:
| Hash | Description |
|------|-------------|
| `75402d4` | Connector PN corrections, 5 connectors flagged, 7 datasheet links |
| `953e033` | TPS25751 WQFN-38 confirmed, DigiKey PN fixed |
| `b3e1800` | Remove premature footprint warnings |
| `1d5e969` | TPD4E05U06QDQARQ1 selected for all 4-ch ESD positions |

markdownlint status: **clean** — only 2 pre-existing acceptable MD013 warnings:
- `design/Guides/User_Manual.md:134`
- `design/Standards/Global_Routing_Spec.md:72`

Currently in progress:
- [ ] Evaluating Vishay MAL222551017E3 as supercap replacement (item B) — web research incomplete at compaction
</work_done>

<technical_details>
**Confirmed stale values — must never reappear:**
- FDC2114RGER (wrong MPN → FDC2114RGHR)
- TPS259807ONRGER (wrong eFuse → TPS259804ONRGER)
- TPD4E05U06DRYR (invalid MPN → TPD4E05U06QDQARQ1)
- TPS25751DREFR-ND / 768-1014-ND / C123467 (old wrong PNs)

**TPD4E05U06QDQARQ1:** Note Mouser PN is `595-PD4E05U06QDQARQ1` (no leading T) — confirmed correct by user directly from Mouser listing page. Do not "correct" this.

**TPS25751DREFR package:** WQFN-38 6×4mm confirmed. No footprint/schematic warnings needed — KiCad projects not yet started, no footprint libraries exist. Package is documented for reference only.

**FDC2114RGHR procurement:** MOQ 4500 at Mouser/DigiKey is irrelevant — all ROT board assembly will go through JLCPCB (C2652079, MOQ 2). No warnings needed in docs.

**Supercap bank design:**
- 6× cells in 2S3P configuration on LTC3350
- Required: 22F / 2.7V per cell (LTC3350 max cell voltage = 2.7V)
- Bank totals: 33F effective at 5.4V
- Hold-up: ≥108.6J, ≥21.7s at 5W CM5 shutdown load
- Charge current limited to 0.5A by LTC3350 RICHARGE resistor
- Original Tecate SCMT32C156PRBA0 does not exist anywhere
- Vishay MAL222551017E3 is being evaluated — Octopart shows Newark stock (SKU 78K8917, ~1,382 units) but full specs not confirmed yet
- Physical constraint: 6 cells must fit within 34mm × 49mm keep-out shadow zone on PM PCB

**Connector issues flagged for redesign:**
- Würth 61201221721 (ROT J_INT 22-pin keyed IDC): MPN does not exist — needs correct MPN or design change
- Molex 22-23-2261 (26-pin shrouded header): wrong part for description
- Molex 22-23-2161 (16-pin shrouded header): wrong part for description
- 1×5 and 1×10 2.54mm Female IDC (JDB J1/J2): no suitable part found — header spec needs redesign

**ERM8-040 vs ERF8-040 DigiKey PN mix-up:** The original doc had SAM8621CT-ND for both ERM8-040 and ERF8-040 — corrected: ERM8-040 = SAM8613CT-ND, ERF8-040 = SAM8621CT-ND.

**markdownlint:** Run via `.\node_modules\.bin\markdownlint.cmd "design/**/*.md"` from repo root. Two pre-existing MD013 warnings are acceptable and should not be fixed.
</technical_details>

<important_files>
- `design/Electronics/Consolidated_BOM.md`
  - Master BOM for all boards — primary reference for all supplier PNs
  - §9 IC/Connector BOM table: all PNs corrected through connector section (#67–#86)
  - §11 Datasheet links: now 34 entries with local PDF paths
  - §1 Component summary table: TPD4E05U06QDQARQ1 and all corrected MPNs
  - Line ~67: supercap row (still TBD PNs for replacement part)
  - Line ~133: Critical Spares section references supercap
- `design/Electronics/Power_Module/Design_Spec.md`
  - Contains supercap bank spec (lines ~87–89): 22F/2.7V, 2S3P, 33F/5.4V, 108.6J hold-up
  - Line ~441: C_SC1–6 BOM row — PNs still TBD pending supercap selection
  - Lines ~444–446: D3/D4/D5 now TPD4E05U06QDQARQ1 ✅
- `design/Electronics/Controller/Design_Spec.md`
  - Line ~503: U4 now TPD4E05U06QDQARQ1 ✅
- `design/Design_Log.md`
  - INC-22: TPD4E05U06QDQARQ1 confirmed ✅
  - DEC-012: TPS25751DREFR WQFN-38 note cleaned up
- `design/Datasheets/`
  - 33 PDFs now tracked in git
  - Still missing: supercap datasheet (pending part selection), TPD4E05U06QDQARQ1 datasheet
</important_files>

<next_steps>
**Immediate — in progress:**
- **Item B: Supercap replacement** — evaluate Vishay MAL222551017E3:
  - Need to confirm: capacitance (should be 22F), voltage rating (need ≥2.7V), package/footprint dimensions (must fit 34mm×49mm keep-out zone, 6 cells), ESR, operating temp range
  - Octopart shows part exists at Newark (SKU 78K8917); need full datasheet specs
  - Once confirmed, update MPN everywhere Tecate SCMT32C156PRBA0 appears and add supplier PNs
  - If not suitable, continue searching (Eaton HV0810-2R7226-R, Panasonic EECS5R5V226, Kemet FY series)

**Remaining review items:**
| # | Item | Action |
|---|------|--------|
| B | Tecate SCMT32C156PRBA0 supercap | **In progress** — evaluating Vishay MAL222551017E3 |
| C | CTS 219-6LPST DIP switch | Confirm DigiKey/JLCPCB PNs |
| D | Würth 61201221721 ROT J_INT | Find correct 22-pin keyed IDC MPN or redesign |
| E | Molex 22-23-2261 26-pin header | Re-identify correct MPN |
| F | Molex 22-23-2161 16-pin header | Re-identify correct MPN |
| G | 1×5 IDC JDB J1 | Redesign header spec |
| H | 1×10 IDC JDB J2 | Redesign header spec |
| J | Marquardt 1800 PM SW1 | Select variant (deferred to mechanical design phase) |

**Still to verify (#87–#99 electromechanical):**
- Würth WE-CMBNC 7448031002 (L1/L2)
- Bourns SRP1265A-100M (L3)
- Coilcraft POE600F-12LD (T2)
- Keystone 1285-ST (ENC BT1–128)
- Keystone 3034 + Renata CR2032 (CTL BT1)
- Würth 9774040151R (CTL standoffs)
- CTS 219-4LPST (STA SW1)
- CTS 219-6LPST (STA/ROT DIP switches)
- Marquardt 1800, ALPS SKRPACE010
- 6.35mm jacks and keyboard switches (already purchased)

**After all parts verified:**
- Create checkpoint
- User will do final manual review of all files
- Declare design complete and proceed to KiCad project setup
</next_steps>
