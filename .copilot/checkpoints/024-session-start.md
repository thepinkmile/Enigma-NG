<overview>
The session is a master parts list verification for the Enigma-NG hardware project — a custom multi-PCB Enigma cipher machine. The user is manually validating every component MPN and supplier PN (DigiKey/Mouser/JLCPCB) against actual distributor listings, and the agent applies all corrections to the design documents. The primary work this segment was replacing the non-existent Tecate supercap with a real part, applying datasheet-derived mechanical specs to the PM design docs, and beginning evaluation of a second alternative supercap.
</overview>

<history>

1. **User provided Vishay MAL222551017E3 DigiKey URL for supercap evaluation**
   - Agent fetched the DigiKey listing and confirmed: 22F/2.7V EDLC, AEC-Q200, THT radial can, 12.5mm dia × 40mm height, −40°C to +85°C
   - Initially flagged THT and 40mm height as concerns; user corrected that SMD is not a requirement, THT is arguably better for mechanical anchoring, MOQ is not an issue (Mouser sells singles), and diameter is just a layout parameter
   - Agent located Mouser PN `594-MAL222551017E3` (240 units in stock) via FindChips; JLCPCB shows 0 stock

2. **User provided all supplier PNs for MAL222551017E3**
   - DigiKey: (blank — not available/OOS), Mouser: `594-MAL222551017E3`, JLCPCB: `C9900091157`
   - Agent replaced all references to Tecate SCMT32C156PRBA0 across 5 files, updated §11 datasheet link (initially to Vishay URL, then updated to local PDF after git detected the file)
   - Commit `8f0df80`

3. **User asked agent to review the datasheet (now present in /design/Datasheets/) and update mechanical specs including rib spacings**
   - Agent extracted text from `Vishay-MAL222551017E3-datasheet.pdf` using pdfminer
   - Key specs extracted: body 12.5mm nominal / 13.0mm max dia, 40mm nominal / 42.5mm max length, lead pitch 5.0mm ±0.5mm, lead dia 0.8mm, mass ≈7g
   - Derived: cell pitch 15mm → **16mm** (to maintain 3mm rib gap with 13mm max body), block footprint 30×45mm → **29×45mm**, keep-out shadow zone 34×49mm → **33×49mm**, enclosure height 42mm → **≥45mm**, Z-height clearance ≥40mm → **≥45mm**, added THT pad spec (5.0mm pitch, 1.0mm drill)
   - Fixed two MD013 lint errors introduced by long lines
   - Commit `26d2112`; markdownlint clean (two known pre-existing warnings only)

4. **User asked whether KYOCERA AVX SCCT35B226SRB would be a better alternative**
   - User provided: DigiKey `478-SCCT35B226SRB-ND`, Mouser `581-SCCT35B226SRB`, no JLCPCB availability
   - Agent extracted datasheet text — this is the "3.0V SCC Series" from KYOCERA AVX
   - Agent fetched FindChips: **480 units in stock at DigiKey**, MOQ 1, ~$4.24 single / ~$2.14 @ 480, 15-week lead time
   - Evaluation was in progress when compaction was triggered — no recommendation or document changes made yet

</history>

<work_done>

Files modified this segment:

- `design/Electronics/Power_Module/Design_Spec.md`
  - MPN: Tecate SCMT32C156PRBA0 → Vishay MAL222551017E3 (THT radial can)
  - Cell pitch: 15mm → 16mm; block footprint: 30×45mm → 29×45mm
  - Keep-out: 34×49mm → 33×49mm
  - Enclosure height: 42mm → ≥45mm internal clearance
  - Z-Height: ≥40mm → ≥45mm with nominal/max dimensions documented
  - THT pad spec added: 5.0mm pitch, 1.0mm drill
  - BOM row C_SC1–6: Tecate TBD → Vishay MAL222551017E3, Mouser 594-MAL222551017E3, JLCPCB C9900091157, package THT Radial Can 12.5mm×40mm

- `design/Electronics/Consolidated_BOM.md`
  - Component count table: Tecate SCMT32C156PRBA0 → Vishay MAL222551017E3
  - Critical Spares note updated: Mouser/JLCPCB source, 10 units
  - S11 supplier entry: Tecate Group → Vishay
  - §11 datasheet row added: `Vishay-MAL222551017E3-datasheet.pdf`

- `design/Electronics/Power_Module/Board_Layout.md`
  - Power chain description: Tecate → Vishay MAL222551017E3
  - Rib clearway note: added 16mm pitch and 13.0mm max body diameter details

- `design/Standards/Certification_Evidence.md`
  - Power chain block diagram: Tecate → Vishay MAL222551017E3

- `design/Datasheets/Vishay-MAL222551017E3-datasheet.pdf` — tracked in git (user added)
- `design/Datasheets/Kyocera-AVX-SCCT35B226SRB-datasheet.pdf` — tracked in git (user added, not yet linked in docs)

Commits this segment:
| Hash | Description |
|------|-------------|
| `8f0df80` | Replace Tecate SCMT32C156PRBA0 with Vishay MAL222551017E3 |
| `26d2112` | Update PM supercap mechanical specs from datasheet |

markdownlint status: **clean** — only two known pre-existing MD013 warnings:
- `design/Guides/User_Manual.md:134`
- `design/Standards/Global_Routing_Spec.md:72`

Currently in progress:
- [ ] KYOCERA AVX SCCT35B226SRB evaluation — comparison vs Vishay, awaiting recommendation decision

</work_done>

<technical_details>

**Vishay MAL222551017E3 — confirmed specs:**
- 22F, 2.7V rated (UCT = 2.3V at 85°C), AEC-Q200
- Body: 12.5mm nominal / 13.0mm max dia × 40mm nominal / 42.5mm max length
- Lead pitch: 5.0mm ±0.5mm; lead dia: 0.8mm; recommended PCB drill: 1.0mm
- Operating temp: −40°C to +85°C (with voltage derating above 65°C)
- Useful life: 1500h @ 85°C (18LL case code)
- Mouser: 240 in stock; JLCPCB: C9900091157 (MOQ 10); DigiKey: OOS/19-week lead time

**KYOCERA AVX SCCT35B226SRB — extracted from datasheet + FindChips:**
- Series: 3.0V SCC (nominal rated voltage is 3.0V — at 2.7V charge we're operating below rated voltage, better for lifetime)
- 22F, tolerance +30%/−10%
- Body: 12.5mm dia × 35mm length (5mm shorter than Vishay — enclosure clearance would drop from ≥45mm to ~≥40mm)
- Lead pitch: **5.5mm** (different from Vishay's 5.0mm — affects PCB footprint)
- Lead dia: 0.8mm (for ≥35mm length parts per datasheet)
- Operating temp: −40°C to +65°C at 3.0V; −40°C to +85°C at 2.5V (at 2.7V charge, temperature derating is between these)
- ESR: Not explicitly given for this specific 35B variant (non-standard vs table entries); the 15F/30mm variant is 50mΩ @ 1kHz
- Endurance/useful life: 1000h at 65°C (high-temp load life test)
- DigiKey: 480 in stock, MOQ 1, ~$4.24 single; 15-week lead time
- Mouser: `581-SCCT35B226SRB`; JLCPCB: not available
- Part number "B" voltage code not standard in the table (only "E"=3.0V shown) — likely a product variant; all evidence confirms it is a 3.0V supercap

**Key trade-off between the two alternatives:**

| Parameter | Vishay MAL222551017E3 | KYOCERA SCCT35B226SRB |
|-----------|----------------------|----------------------|
| Voltage | 2.7V (matches LTC3350 max exactly) | 3.0V (operating at 2.7V = 90% rated — better lifetime) |
| Body height | 40mm (max 42.5mm) | 35mm (max 37mm) |
| Enclosure clearance needed | ≥45mm | ~≥40mm |
| Lead pitch | 5.0mm | 5.5mm |
| DigiKey stock | OOS / 19-week LT | 480 in stock, MOQ 1 |
| Mouser stock | 240 units | Available (581-SCCT35B226SRB) |
| JLCPCB | C9900091157 (MOQ 10) | Not available |
| AEC-Q200 | Yes | Not stated explicitly |
| Useful life | 1500h @ 85°C | 1000h @ 65°C |

**Supercap bank design (unchanged):** 6× cells, 2S3P, 33F effective at 5.4V, 108.6J hold-up, ≥21.7s at 5W load, LTC3350-managed, RICHARGE = 0.5A charge current limit.

**Confirmed stale values — never reappear:**
- Tecate SCMT32C156PRBA0 (replaced globally)
- Old enclosure height "42mm" (now ≥45mm)
- Old block footprint "30×45mm" (now 29×45mm)
- Old keep-out "34×49mm" (now 33×49mm)
- Old cell pitch "15mm" (now 16mm)

**markdownlint:** Run via `$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine")+";"+[System.Environment]::GetEnvironmentVariable("PATH","User"); cd repo && .\node_modules\.bin\markdownlint.cmd "design/**/*.md" --fix && .\node_modules\.bin\markdownlint.cmd "design/**/*.md"`

</technical_details>

<important_files>

- `design/Electronics/Power_Module/Design_Spec.md`
  - Primary PM specification — contains supercap bank spec, BOM, Z-height, enclosure clearance, rib clearway, keep-out zone
  - All supercap mechanical specs updated this segment
  - Key sections: §1 (PCB Spec lines ~68–83), §2 Power & UPS Hub (lines ~85–107), BOM C_SC1–6 row (~line 441)

- `design/Electronics/Consolidated_BOM.md`
  - Master BOM for all boards — primary reference for all supplier PNs
  - Supercap row updated; S11 supplier entry replaced; §11 datasheet link added
  - Key lines: ~67 (component count), ~133 (critical spares), ~325 (supplier S11), ~376 (§11 new datasheet row)

- `design/Electronics/Power_Module/Board_Layout.md`
  - Power chain description and rib clearway note updated with new pitch/diameter
  - Key lines: ~71 (block description), ~165–166 (power chain), ~171–174 (rib clearway note)

- `design/Datasheets/Vishay-MAL222551017E3-datasheet.pdf`
  - Local PDF for the selected supercap — Vishay ENYCAP 225 EDLC-R series
  - Linked in Consolidated_BOM §11

- `design/Datasheets/Kyocera-AVX-SCCT35B226SRB-datasheet.pdf`
  - Alternative supercap datasheet added by user — not yet linked in docs
  - Evaluation in progress

- `design/Standards/Certification_Evidence.md`
  - Power chain block diagram updated: Tecate → Vishay MAL222551017E3 (~line 102)

</important_files>

<next_steps>

**Immediate — in progress:**

- **Supercap decision: KYOCERA SCCT35B226SRB vs Vishay MAL222551017E3**
  - Evaluation was underway when compaction triggered
  - Key finding: KYOCERA is 5mm shorter (35mm vs 40mm), has 3.0V rating (operating below rated at 2.7V charge = better lifetime), is in stock at DigiKey (480 units, MOQ 1), but has a different lead pitch (5.5mm vs 5.0mm) and no JLCPCB availability
  - Need to present recommendation to user and, if KYOCERA is chosen, update all docs again (cell pitch to 5.5mm→17mm centre-to-centre to maintain 3mm rib gap with 13mm body, or adjust; enclosure to ≥40mm; MPN/PNs everywhere)
  - Need to link KYOCERA datasheet in Consolidated_BOM §11 if selected
  - **User has not yet decided** — awaiting the comparison recommendation

**Remaining parts verification items (after supercap decision):**
| # | Item | Action needed |
|---|------|--------------|
| B | Supercap | **Decision pending** — KYOCERA vs Vishay |
| C | CTS 219-6LPST DIP switch | Confirm DigiKey/JLCPCB PNs |
| D | Würth 61201221721 ROT J_INT | Find correct 22-pin keyed IDC MPN or redesign |
| E | Molex 22-23-2261 26-pin header | Re-identify correct MPN |
| F | Molex 22-23-2161 16-pin header | Re-identify correct MPN |
| G | 1×5 IDC JDB J1 | Redesign header spec |
| H | 1×10 IDC JDB J2 | Redesign header spec |
| J | Marquardt 1800 PM SW1 | Deferred to mechanical design phase |

**After all parts verified:**
- Create checkpoint
- User manual review of all files
- Declare design complete → proceed to KiCad project setup

</next_steps>