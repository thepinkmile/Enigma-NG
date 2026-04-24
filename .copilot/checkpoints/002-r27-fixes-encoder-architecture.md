<overview>
This session continues the Enigma-NG electronics design documentation review cycle, with three parallel goals: (1) close the ongoing multi-round content review cycle by achieving two consecutive clean passes, (2) apply a supercapacitor bank upgrade from 2×2 to 2×3 layout with a 3mm inter-cell gap, and (3) correct and significantly expand the Encoder board architecture documentation based on design clarifications from the project owner. The approach uses background agents for review passes and fix commits, with careful false-positive filtering (especially the eFuse cluster), while the user and assistant discuss architecture in parallel.
</overview>

<history>
1. **Session alignment** — user asked to review previous session states and align with planned next steps.
   - Read plan.md and checkpoint 001; confirmed R26+R27 were needed for two consecutive clean passes.
   - Set up SQL todos; marked `review-cycle-close` and `encoder-detailed-design` in_progress.
2. **R26 deep-dive review launched** (background agent)
   - While running, user discussed QUE-001 (supercap rib clearway ENIG bonding).
3. **DEC-020 decision applied** — user confirmed: YES to ENIG strips (1.5mm min, GND_CHASSIS net), YES to Kapton tape (min 2-mil/50µm polyimide wrapped around supercap bodies), YES to conductive elastomer gasket (≤3mm wide after gap increase), Faraday cage intent noted.
4. **R26 results received** — 20 claimed findings; 14 were FALSE POSITIVES (agent tried to revert TPS259804ONRGER → TPS259807ONRGER). 6 genuine findings fixed: CTL Design_Spec/Board_Layout L6 label, Design_Log INC-22 TPD4E05U06 suffix (→DRYR), PM Design_Spec D3/D4/D5 suffix (→DRYR), DEC-020 fully written. Committed as `ab7452f`.
5. **Supercap 2×3 discussion** — user confirmed 2×2 was wrong; intent was always 2×3 2S3P.
   - Calculated: 33F at 5.4V, ≥21.7s hold-up @ 5W, 108.6J energy.
   - User then asked: increase inter-cell gap to 3mm for safety (Kapton + gasket clearance).
   - Final geometry: 15mm pitch, 30×45mm block, 34×49mm shadow zone, 3.0mm gap.
   - Two agents ran sequentially: `supercap-2x3-change` (committed with 2mm gap / old values) then `supercap-2x3-upgrade` (corrected to 3mm gap values). Second agent also inserted DEC-021 and renumbered prior DEC-021/022/023 (JDB entries) to DEC-022/023/024.
6. **Encoder architecture discussion** — user corrected multiple misconceptions:
   - **Correction 1:** CPLDs are NOT split left-32/right-32 by character range. Instead: CPLD1 = Decode Half (ENC_IN → 64 lines), CPLD2 = Encode Half (64 lines → ENC_OUT). Serial flow through jacks.
   - **Correction 2:** Only 2 rows of 64 spade terminals (128 total), not 4 rows (256). BT129–256 do not exist. Keyboard switches connect to BT65–128; lamp lines connect to BT1–64.
   - **Correction 3:** Two halves are completely electrically independent on PCB. The ONLY connection between them is J2 (shared power, both 6-bit buses, JTAG).
   - **Jack wiring clarification:** Tip+Switch → CPLD A (BT1–64); Sleeve → CPLD B (BT65–128). No plug = N/C Switch→Sleeve = identity. Crossover cable (Tip-A → Sleeve-B) = passive reciprocal substitution. Max 32 cables.
   - **Plugboard system context:** Enigma-NG uses 2 Encoder boards. Stator CPLD routes signal chain — J5/J6 can be placed at any configurable position. Original Enigma = double pass (after keyboard + before lightboard); later models = single pass at reflector; Enigma-NG = fully configurable.
7. **Documentation improvement plan agreed** — user agreed to all suggested changes:
   - §1 Overview: two-half architecture + plugboard system context + historical table
   - §3: rewrite with Decode/Encode half definitions + signal flow diagrams
   - §4: fix spade terminal descriptions, add Jack Wiring section, flag insertion detect as open item
   - §9: add silkscreen labelling note (DECODE/ENCODE)
   - BOM: remove BT129–256, fix R9→R72 (64×), C22→C85 (64×), fix J1 description
   - Stator: add plugboard routing configuration context to J4/J5/J6 description + FR-STA-05
8. **R27 launched** (background, completed — 16 findings, all genuine)
   - Root cause: DEC-021 insertion shifted JDB decisions from DEC-021/022/023 → DEC-022/023/024; cross-references not updated.
   - Findings: TPD4E05U06DBVR stale in CTL BOM (×2), DEC number off-by-one in JDB Design_Spec (×10), CTL Design_Spec/Board_Layout (×3).
9. **encoder-stator-fix launched** (background, still running at compaction time)
   - Applies all Encoder §1/§3/§4/§9/BOM corrections and Stator J4/J5/J6 routing context.
10. **Completion plan agreed** — user confirmed: after encoder-stator-fix commits, run a full R28+R29 review cycle (not just R27+R28), since new content needs its own clean passes before saving checkpoint.
</history>

<work_done>
Files modified this session:

- `design/Electronics/Controller/Design_Spec.md` — L6 label fix §9.2; DEC-023→DEC-024 fix pending (R27 finding #14)
- `design/Electronics/Controller/Board_Layout.md` — L6 label fix §9 stackup; DEC-023→DEC-024 fix pending (R27 findings #15, #16)
- `design/Design_Log.md` — INC-22 suffix fix; QUE-001 closed; DEC-020 written; DEC-021 (supercap upgrade) inserted; JDB decisions renumbered to DEC-022/023/024
- `design/Electronics/Power_Module/Design_Spec.md` — D3/D4/D5 DRYR suffix; DEC-020 Kapton/ENIG/gasket bullets; full 2×3 supercap upgrade (6 cells, 33F, 30×45mm, 34×49mm, 3.0mm gap, ≥21.7s, 108.6J, DEC-020 gap refs updated)
- `design/Electronics/Power_Module/Board_Layout.md` — DEC-020 rib clearway note; 2×3 ASCII diagram updates
- `design/Electronics/Consolidated_BOM.md` — qty 4→6, C_SC1–4→C_SC1–6
- `design/Standards/Certification_Evidence.md` — 2S2P→2S3P, ≥14.5s→≥21.7s, ~2min→~3min
- `design/Guides/User_Manual.md` — 4→6 cells, 2S2P→2S3P, 22F→33F, all hold-up/charge time refs updated
- `design/Software/Linux_OS/Power_Management.md` — all ≥14.5s→≥21.7s refs updated
- `design/Electronics/Boards_Overview.md` — 22F→33F, ≥14.5s→≥21.7s
- `design/Electronics/Encoder/Design_Spec.md` — **IN FLIGHT** (encoder-stator-fix agent): §1/§3/§4/§9 rewrites, BOM corrections (remove BT129–256, R9→R72, C22→C85, fix J1/BT descriptions)
- `design/Electronics/Stator/Design_Spec.md` — **IN FLIGHT** (encoder-stator-fix agent): FR-STA-05 expansion, plugboard routing context section

Commits this session:
- `ab7452f` — R26 fixes (6 findings) + DEC-020 decision
- supercap 2×3 upgrade commit — DEC-021, all 8 files updated with 3mm gap / 30×45mm / ≥21.7s values

Tasks:
- [x] R26 review run and genuine fixes applied
- [x] DEC-020 written (QUE-001 closed)
- [x] Supercap 2×3 2S3P upgrade across all docs (3mm gap, 30×45mm, 34×49mm, ≥21.7s)
- [x] R27 launched and completed (16 findings — all genuine, root cause = DEC renumbering)
- [ ] R27 findings fix (16 findings need applying — TPD4E05U06 suffix ×2, DEC cross-refs ×14)
- [ ] encoder-stator-fix commit (in flight)
- [ ] R28 review (first post-encoder-fix pass)
- [ ] R29 review (second consecutive clean pass)
- [ ] Encoder marked complete
- [ ] Checkpoint saved
</work_done>

<technical_details>
**eFuse — CRITICAL: TPS259804ONRGER is correct, TPS259807ONRGER is STALE**
- TPS259804ONRGER: silicon-fixed 16.9V OVLO — correct; must never be changed
- TPS259807ONRGER: stale, must never reappear; R26 agent tried to reinstate it (14 false positives)

**TPD4E05U06 suffix — DRYR is correct for U-DFN-10**
- DRYR = U-DFN-10 (10-pin, correct). DBVR = SOT-23-5 (wrong). DQAR/DQNR = also wrong.
- Mouser: 595-TPD4E05U06DRYR; DigiKey: 296-TPD4E05U06DRYRCT-ND; JLCPCB: C123462
- R27 found stale DBVR in CTL Design_Spec BOM (U4) and DQNR in Consolidated_BOM §5.1

**DEC renumbering cascade — R27 root cause**
- DEC-021 (supercap upgrade) was inserted by the upgrade agent, shifting prior JDB decisions:
  - Crystal clock: was DEC-021, now DEC-022
  - GND_CHASSIS: was DEC-022, now DEC-023
  - JTAG buffer/master: was DEC-023, now DEC-024
- All cross-references in JDB Design_Spec, JDB Board_Layout, CTL Design_Spec, CTL Board_Layout need updating (16 instances total across R27 findings #3–#16)

**Supercap 2×3 2S3P geometry (final confirmed values)**
- 6× Tecate TPLH-2R7/22WR12X31 (22F/2.7V each)
- Configuration: 2S3P = 33F effective at 5.4V
- Inter-cell gap: 3.0mm; pitch: 15mm; block: 30×45mm; shadow zone: 34×49mm
- Hold-up: ≥21.7s at 5W (108.6J); charge time: ~3 min from depleted
- BOM order qty stays 10 (MOQ) — 6 production + 2 spares + 2 testing = 10 exactly
- Designators: C_SC1–6

**DEC-020 rib clearway specs (final)**
- ENIG strip: min 1.5mm wide × full rib depth, L1, GND_CHASSIS net
- Kapton tape: min 2-mil (50µm) polyimide, wrapped around supercap bodies
- Conductive gasket: ≤3mm wide (increased from ≤2mm due to 3mm gap), self-adhesive elastomer/foam, part TBD at mechanical design phase
- Faraday cage intent: ENIG bonding + gasket + Kapton insulation creates RF shielding around supercap block

**Encoder board — two-half architecture (CORRECTED understanding)**
- Two completely independent halves; no PCB copper between them except J2
- Decode Half (U1/CPLD A): ENC_IN[0:5] → 64 output lines → BT1–64 spade terminals
- Encode Half (U2/CPLD B): BT65–128 spade terminals → 64 input lines → ENC_OUT[0:5]
- J2 is the ONLY connection: carries 3V3_ENIG, GND, ENC_IN[0:5], ENC_OUT[0:5], JTAG chain
- JTAG: J2 TDI → U1 → U1 TDO → R7(33Ω) → U2 TDI → U2 TDO → R8(75Ω) → J2 TDO
- Spade terminals: 2 rows × 64 = 128 total. BT129–256 DO NOT EXIST.

**Encoder jack wiring (plugboard mode)**
- Each jack: Tip+Switch → CPLD A output (BT1–64, same node); Sleeve → CPLD B input (BT65–128)
- No plug: N/C Switch→Sleeve = identity passthrough (passive)
- Cable: crossover wiring (Tip-A → Sleeve-B); passive reciprocal substitution; max 32 cables
- Physical harness = mechanical design item (Mechanical/Plugboard/Design_Spec.md)
- Insertion detect: Switch opens when plug inserted — monitoring path is an open item

**Plugboard system context**
- Enigma-NG uses up to 2 Encoder boards (one per plugboard pass)
- Stator CPLD routes 6-bit bus; J4=HID, J5=Plugboard Pass A, J6=Plugboard Pass B
- Pass positions are fully configurable: original Enigma (after keyboard + before lightboard), later Enigma (at reflector only), or any custom configuration

**BOM corrections for Encoder (post-fix)**
- Pull-up resistors: R9–R72 (64× only, Encode Half inputs); was R9–R136 (128×, wrong)
- RC filter caps: C22–C85 (64× only); was C22–C149 (128×, wrong)
- Decode Half outputs driven by CPLD A — no pull-ups or RC filters needed on BT1–64

**Review cycle lint method**
- ide-get_diagnostics ONLY (Node.js not on PATH — npx/markdownlint CLI fails)
- Two consecutive clean passes required (content + lint) to close design phase

**False positive pattern: eFuse cluster**
- Any agent without explicit stale-values context will try to reintroduce TPS259807ONRGER
- Always cross-reference stale values master list before applying eFuse findings
</technical_details>

<important_files>
- `design/Design_Log.md`
  - Master log of all decisions (DEC-xxx), incidents (INC-xxx), questions (QUE-xxx)
  - Modified: INC-22 suffix fix; QUE-001 closed; DEC-020 written; DEC-021 supercap upgrade added; JDB decisions renumbered DEC-022/023/024
  - Key: DEC-020 (~rib clearway), DEC-021 (~supercap upgrade), DEC-022 (~crystal clock), DEC-023 (~GND_CHASSIS), DEC-024 (~JTAG buffer)
- `design/Electronics/Power_Module/Design_Spec.md`
  - Core PM spec; all supercap, eFuse, DEC-020 details
  - Modified: DRYR suffix, DEC-020 bullets, full 2×3 upgrade
  - Key: DR-PM-07 (supercap spec), §4 (supercap block + rib clearway), BOM (C_SC1–6, D3/D4/D5)
- `design/Electronics/Encoder/Design_Spec.md`
  - **IN FLIGHT** — encoder-stator-fix agent currently applying major rewrites
  - Changes: §1 Overview (two-half architecture + plugboard context), §3 (signal flow diagrams), §4 (spade terminal fix, jack wiring section), §9 (silkscreen labelling), BOM (remove BT129–256, fix R/C counts, fix J1 description)
  - Current BOM has incorrect BT129–256 rows and R9–R136 / C22–C149 (all 128× — should be 64×)
- `design/Electronics/Stator/Design_Spec.md`
  - **IN FLIGHT** — encoder-stator-fix agent adding plugboard routing context
  - Changes: FR-STA-05 expansion, new plugboard routing section (J5/J6 configurable positions, historical reference table)
- `design/Electronics/JTAG_Daughterboard/Design_Spec.md`
  - R27 found DEC cross-reference errors (findings #3–#5, #6–#8, #10–#13): DEC-021→022, DEC-022→023, DEC-023→024 throughout
  - Needs R27 fix pass before R28 launches
- `design/Electronics/JTAG_Daughterboard/Board_Layout.md`
  - R27 finding #9: DEC-022→DEC-023 for GND_CHASSIS reference
- `design/Electronics/Controller/Design_Spec.md`
  - R27 finding #1 (DBVR→DRYR in U4 BOM row) and #14 (DEC-023→DEC-024 JTAG cross-ref)
- `design/Electronics/Controller/Board_Layout.md`
  - R27 findings #15, #16: DEC-023→DEC-024 in JTAG routing table and note
- `design/Electronics/Consolidated_BOM.md`
  - R27 finding #2: TPD4E05U06DQNR→DRYR in §5.1 Controller section
- `%USERPROFILE%\.copilot\session-state\<session-id>\plan.md`
  - Session plan updated this session with full todo list and revised completion sequence
</important_files>

<next_steps>
**Immediate — fix R27's 16 findings:**
Apply all 16 R27 findings in a single fix commit:
- Finding #1: CTL Design_Spec U4 BOM: `595-TPD4E05U06DBVR` → `595-TPD4E05U06DRYR`; `296-TPD4E05U06DBVRCT-ND` → `296-TPD4E05U06DRYRCT-ND`
- Finding #2: Consolidated_BOM §5.1: `TPD4E05U06DQNR` → `TPD4E05U06DRYR`
- Findings #3–#5: JDB Design_Spec crystal clock refs: `DEC-021` → `DEC-022` (×3)
- Findings #6–#9: JDB Design_Spec + Board_Layout GND_CHASSIS refs: `DEC-022` → `DEC-023` (×4)
- Findings #10–#13: JDB Design_Spec JTAG buffer refs: `DEC-023` → `DEC-024` (×4 in DR table + §6 + BOM)
- Findings #14–#16: CTL Design_Spec + Board_Layout JTAG refs: `DEC-023` → `DEC-024` (×3)

**Wait for encoder-stator-fix agent to complete**, then verify commit.

**After both fixes committed — launch R28:**
Full deep-dive review across all docs including new Encoder/Stator architecture content.
Must be clean (zero findings).

**After R28 clean — launch R29:**
Second consecutive clean pass. Must also be clean.

**After R28+R29 both clean:**
1. Add Design_Log entry marking Encoder detailed design complete
2. Update board status table in plan.md: Encoder → ✅ Complete
3. Save session checkpoint titled appropriately
4. Update plan.md next steps: Rotor detailed design review

**Open items logged (not blocking):**
- Encoder insertion detect monitoring path (open item in Mechanical/Plugboard/Design_Spec.md)
- Supercap mounting orientation (vertical implied, not documented; retention clip for vibration)
- OWI-001/002/003/018 still open
- SW1 vintage switch selection
- ERA-3ARB2672V/ERA-3ARB1002V MOQ issue (R14/R15 LTC3350 divider)
- Rotor detailed design review (next major phase after checkpoint)
</next_steps>
