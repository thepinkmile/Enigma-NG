<overview>
The session is a master parts list verification for the Enigma-NG hardware project. The user is manually confirming every component MPN and supplier PN (DigiKey/Mouser/JLCPCB) against actual distributor listings, and the agent applies all corrections to the design documents. The primary work this segment was selecting the final supercapacitor (evaluating three alternatives: Vishay, KYOCERA AVX, and Abracon), switching all design docs to the Abracon ADCR-T02R7SA256MB, and beginning connector/switch PN verification.
</overview>

<history>

1. **Supercap evaluation — Vishay MAL222551017E3 (already selected in prior segment)**
   - Prior segment had replaced Tecate with Vishay and updated all mechanical specs
   - Vishay was the baseline entering this segment
2. **User proposed KYOCERA AVX SCCT35B226SRB as alternative**
   - Agent fetched FindChips and datasheet, confirmed: 22F, 3.0V rated, 12.5mm×35mm body, 5.5mm lead pitch
   - DigiKey: 480 in stock; Mouser: 581-SCCT35B226SRB; JLCPCB: not available
   - Key specs: derated above 65°C at 3.0V (≤2.5V at 85°C); KiCAD model available via Mouser
   - Compared vs Vishay: KYOCERA shorter (37mm vs 42.5mm max), 3.0V rated = 10% voltage margin at 2.7V charge
3. **User proposed Abracon ADCR-T02R7SA256MB as third alternative**
   - Described as 25F (not 22F) — user asked if the difference matters
   - Agent confirmed via FindChips and Farnell: 25F, 2.7V, THT radial, 16mm dia × 25mm height, 7.5mm lead pitch, ESR 30mΩ
   - Agent read the datasheet (ADCR-T02R7S-datasheet.pdf): confirmed D=16.0±0.5mm, L=25.0±2.0mm, P=7.5±0.5mm, d=0.8mm, operating temp −40°C to +85°C (no derating mentioned), ±20% tolerance
   - 25F vs 22F: strictly better — bank becomes 37.5F, energy 123.8J, hold-up 24.8s (vs 21.7s)
4. **Three-way comparison and decision**
   - User noted KYOCERA also has KiCAD model via Mouser (neutralising that Abracon advantage)
   - User questioned the ⚠️ warning on 2.7V-rated parts — correctly pointing out the design was always for 2.7V
   - Agent clarified: 2.7V parts operating at rated voltage is correct; KYOCERA 3.0V just has extra margin, no design change needed
   - User noted longevity comparison is not straightforward without explicit hours figures for Abracon
   - Agent pointed out KYOCERA is derated above 65°C at 3.0V — at 2.7V charge, safe max temp is unspecified between 65–85°C, while Abracon is explicitly confirmed at 2.7V + 85°C
   - **User decided: Abracon ADCR-T02R7SA256MB**
5. **User confirmed to switch to Abracon and remove redundant datasheets**
   - Agent applied all changes across 5 files (see Work Done)
   - Deleted Vishay-MAL222551017E3-datasheet.pdf (was committed); deleted Kyocera-AVX-SCCT35B226SRB-datasheet.pdf (was untracked, removed from disk)
   - Added ADCR-T02R7S-datasheet.pdf
   - Ran markdownlint — one new lint error on BOM line 133 (line too long), fixed by wrapping
   - Committed as `d74eeea`
6. **User asked what other items remain for review**
   - Agent reviewed session history and listed items C–J plus passives from #28 onwards
7. **Item C — CTS DIP switch confirmed**
   - User confirmed: MPN 219-6LPSTR (note: R suffix = tape-and-reel variant of 219-6LPST)
   - Supplier PNs: DigiKey=119-219-6LPSTRCT-ND, Mouser=774-2196LPSTR, JLCPCB=C2842671
   - Datasheet downloaded (CTS-Switches-DIP-219-Series-Datasheet.pdf)
   - No KiCAD footprint available from manufacturer — likely uses generic KiCAD DIP footprint
   - Agent searched all references to 219-6LPST in design docs; also found 219-4LPST (Stator SW1) which is a different part and not under review
   - **Update not yet applied** — compaction triggered mid-task

</history>

<work_done>

Files modified this segment (all committed in `d74eeea`):

- `design/Electronics/Power_Module/Design_Spec.md`
  - MPN: Vishay MAL222551017E3 → Abracon ADCR-T02R7SA256MB
  - Cell pitch: 16mm → 20mm; block footprint: 29×45mm → 37×57mm; keep-out: 33×49mm → 41×61mm
  - Enclosure Z-clearance: ≥45mm → ≥30mm; body spec: 12.5mm×40mm → 16.0mm×25.0mm
  - THT pad: 5.0mm pitch → 7.5mm pitch (1.0mm drill unchanged)
  - Bank: 33F → 37.5F; energy: 108.6J → 123.8J; hold-up: ≥21.7s → ≥24.8s (all instances)
  - BOM row C_SC1–6: Mouser=815-ADCRT02R7SA256MB, DigiKey=535-ADCR-T02R7SA256MB-ND, JLCPCB=Global sourcing
- `design/Electronics/Consolidated_BOM.md`
  - Component count row: Vishay MAL222551017E3 → Abracon ADCR-T02R7SA256MB, 22F → 25F
  - Critical spares §1: updated source/PNs, noted JLCPCB global sourcing only
  - S11 supplier: Vishay → Abracon with new URL and notes
  - §11 datasheet row: Vishay PDF → ADCR-T02R7S-datasheet.pdf
- `design/Electronics/Power_Module/Board_Layout.md`
  - Power chain: Vishay → Abracon ADCR-T02R7SA256MB
  - Rib clearway note: 16mm pitch / 13.0mm max → 20mm pitch / 16.5mm max
- `design/Standards/Certification_Evidence.md`
  - Power chain block: Vishay → Abracon ADCR-T02R7SA256MB, 33F → 37.5F
- `design/Datasheets/Vishay-MAL222551017E3-datasheet.pdf` — deleted (git rm)
- `design/Datasheets/Kyocera-AVX-SCCT35B226SRB-datasheet.pdf` — deleted (was untracked)
- `design/Datasheets/ADCR-T02R7S-datasheet.pdf` — added (git add)

**In progress at compaction:**
- Item C (CTS 219-6LPSTR DIP switch): user confirmed MPN and PNs, datasheet present, update NOT yet applied

**markdownlint status:** Only two pre-existing warnings remain:
- `design/Guides/User_Manual.md:134`
- `design/Standards/Global_Routing_Spec.md:72`

</work_done>

<technical_details>

**Abracon ADCR-T02R7SA256MB — confirmed from datasheet:**
- 25F, 2.7V, ±20% tolerance
- D = 16.0±0.5mm (max 16.5mm), L = 25.0±2.0mm (max 27.0mm)
- Lead pitch P = 7.5±0.5mm, lead dia d = 0.8±0.05mm → recommended PCB drill 1.0mm
- ESR max: 30mΩ; Leakage: 0.070mA; Peak current: 19.29A
- Operating temp: −40°C to +85°C at full 2.7V (no derating stated)
- ISO9001-2015 certified; RoHS compliant; MSL Level 1
- Packaging: 250 pcs/bag (bulk)

**Bank design (2S3P with Abracon):**
- 3 cells in parallel per string × 2 strings in series
- Bank C = 25F × 3 / 2 = 37.5F at 5.4V
- Energy = ½ × 37.5 × (5.4² − 4.75²) = 123.8J
- Hold-up at 5W = 123.8 / 5 = 24.8s
- Cell pitch = 16.5mm max body + 3.5mm rib gap = 20mm
- Block (3 cols × 2 rows): width = 2×20 + 16.5 = 56.5mm ≈ 57mm; depth = 1×20 + 16.5 = 36.5mm ≈ 37mm
- Keep-out = 37+4 × 57+4 = 41×61mm

**Supercap rated voltage clarification:**
- 2.7V-rated parts running at 2.7V charge = operating at rated voltage — this is correct and expected
- 3.0V-rated KYOCERA at 2.7V charge = operating at 90% rated — slight longevity benefit but no design change needed
- KYOCERA caveat: derated above 65°C at 3.0V; at 2.7V the safe max temp is unspecified (between 65–85°C)
- Abracon advantage: explicitly confirmed 2.7V + 85°C — matches design operating conditions exactly

**CTS 219-6LPSTR (Item C):**
- MPN suffix "R" = tape-and-reel variant of 219-6LPST
- DigiKey: 119-219-6LPSTRCT-ND; Mouser: 774-2196LPSTR; JLCPCB: C2842671
- Datasheet: CTS-Switches-DIP-219-Series-Datasheet.pdf (present in design/Datasheets/)
- Used as SW2 on Stator (6-position) and SW1/SW2/SW3 on Rotor (6-position each)
- Note: Stator SW1 uses 219-4LPST (4-position) — different part, different PNs, not under review here

**JLCPCB global sourcing:**
- When a part has no JLCPCB stock listing, it can be sourced globally via DigiKey or Mouser through JLCPCB's global sourcing service
- BOM column entry: "Global sourcing" with DigiKey/Mouser PNs in their respective columns

**markdownlint rules:**
- MD013: line length ≤200 characters — must wrap long BOM/notes lines manually (--fix doesn't handle table rows)
- Run via: `$env:PATH = ...; .\node_modules\.bin\markdownlint.cmd "design/**/*.md" --fix` then without --fix

**Stale values (must never reappear):**
- Tecate SCMT32C156PRBA0, Vishay MAL222551017E3 (both replaced)
- Old enclosure: 42mm or 45mm (now ≥30mm)
- Old block footprint: 29×45mm, old keep-out: 33×49mm, old cell pitch: 15mm or 16mm
- Old hold-up: 21.7s; old energy: 108.6J; old bank: 33F

</technical_details>

<important_files>

- `design/Electronics/Power_Module/Design_Spec.md`
  - Primary PM specification — supercap bank, BOM, Z-height, enclosure clearance, rib clearway, keep-out
  - All supercap specs updated to Abracon this segment
  - Key sections: §1 PCB Spec (~lines 71–86), §2 Power & UPS Hub (~lines 90–92, 108–109), §5 Supercap Manager (~lines 218, 238), BOM C_SC1–6 (~line 445)
- `design/Electronics/Consolidated_BOM.md`
  - Master BOM — primary reference for all supplier PNs across all boards
  - Supercap row, critical spares, S11 supplier, datasheet link all updated
  - Key lines: ~67 (component count), ~133–134 (critical spares), ~325 (S11), ~376 (datasheet row)
- `design/Electronics/Power_Module/Board_Layout.md`
  - Power chain and rib clearway note updated
  - Key lines: ~166 (power chain), ~172 (rib clearway)
- `design/Datasheets/ADCR-T02R7S-datasheet.pdf`
  - Abracon supercap series datasheet — source of mechanical specs
  - Added this segment; linked in Consolidated_BOM §11
- `design/Datasheets/CTS-Switches-DIP-219-Series-Datasheet.pdf`
  - DIP switch datasheet for 219-6LPSTR (and 219-4LPST)
  - Present but not yet linked in docs
- `design/Electronics/Stator/Design_Spec.md`
  - SW2 (219-6LPST→219-6LPSTR) BOM row needs updating (~line 315)
  - SW1 (219-4LPST) is a separate part — not under review
- `design/Electronics/Rotor/Design_Spec.md`
  - SW1/SW2/SW3 all reference 6-position DIP switch with TBD PNs (~line 480) — needs updating

</important_files>

<next_steps>

**Immediate — in progress:**

**Item C: Apply CTS 219-6LPSTR update to design docs**
- Confirmed MPN: 219-6LPSTR; DigiKey: 119-219-6LPSTRCT-ND; Mouser: 774-2196LPSTR; JLCPCB: C2842671
- Files to update:
  - `Stator/Design_Spec.md` line ~315: SW2 BOM row — replace `219-6LPST` / `774-219-6LPST` / TBD / TBD
  - `Rotor/Design_Spec.md` line ~480: SW1/SW2/SW3 BOM rows — fill in MPN and all supplier PNs
  - `Consolidated_BOM.md`: add/update 219-6LPSTR row with supplier PNs
  - Link CTS datasheet in Consolidated_BOM §11
  - Note: no footprint from manufacturer — relies on generic KiCAD DIP-6 footprint

**Remaining parts verification items:**
| # | Item | Action needed |
|---|------|--------------|
| D | Würth 61201221721 (ROT J_INT) | Find correct 22-pin keyed IDC MPN or redesign |
| E | Molex 22-23-2261 (26-pin header) | Re-identify correct MPN |
| F | Molex 22-23-2161 (16-pin header) | Re-identify correct MPN |
| G | 1×5 2.54mm Female IDC (JDB J1) | Re-think header spec |
| H | 1×10 2.54mm Female IDC (JDB J2) | Re-think header spec |
| J | Marquardt 1800 (PM SW1) | Deferred to mechanical design phase |

**Then:** Passive components from #28 onwards — user to continue providing verified PNs

**After all parts verified:**
- Create checkpoint
- Rotor single-side JLCPCB constraint resolution (plan.md open item)
- Rotor detailed design review cycle (2 clean passes)
- KiCad project setup

</next_steps>
