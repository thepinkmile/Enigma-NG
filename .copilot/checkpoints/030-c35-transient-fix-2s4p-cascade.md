<overview>
This session segment focused on resolving three root causes of recurring design regressions in the Enigma-NG power module documentation (eFuse MPN swapping, supercap values reverting, Extension U1 buffer being removed), upgrading the supercap bank from 2S3P to 2S4P (8 cells, 50F) after correcting the load assumption from 5W to 15W, and discovering a new transient margin issue on 5V_MAIN during LTC3350 backup switchover at 3A load. The approach was to lock in the correct values with explicit warning blocks in the design docs, create authoritative Design Decisions (DEC-029), and systematically cascade all changes across the full document set. A new capacitor C35 and resistor changes (R14, R30) are pending implementation to fix the backup switchover transient.
</overview>

<history>

1. **User asked why the eFuse MPN keeps changing (TPS259804 ↔ TPS259807)**
   - Confirmed TPS259804ONRGER is correct (16.9V silicon-fixed OVLO, cut-tape)
   - TPS259807 = no OVLO (wrong), TPS259803 = no OVLO (wrong)
   - Added `⚠️ eFuse variant lock` block to PM/Design_Spec.md BOM notes and DEC-005
   - Added Part Number Change Rule: datasheet must exist in `design/Datasheets/` before any MPN change

2. **User asked about supercap stale values and Extension U1 removal root causes**
   - **Extension root cause:** §5 said "Passive components only." — review agents read this as no active components and removed U1 (SN74LVC2G125DCUR). Fixed: explicit "U1 is the only active IC" + NEVER REMOVE warning
   - **Supercap root cause:** PM/Design_Spec.md had correct Abracon 25F values but 6 other docs still had stale 22F/33F/21.7s — review agents "corrected" PM back to match the majority. Fixed: swept all files to 25F/37.5F/24.8s

3. **User asked to create DEC-029 as authoritative supercap spec, obsolete DEC-004 and DEC-021**
   - DEC-004 marked Superseded by DEC-029 (0.5A charge current retained)
   - DEC-021 marked Superseded by DEC-029 (2S3P arrangement retained)
   - DEC-029 created with 2S3P, 5W load — later discovered this was wrong

4. **User corrected load: CM5 draws 3A at 5V = 15W, not 5W**
   - Recalculated: 2S3P (37.5F) at 15W → realistic hold-up = 25.2s (only 26% margin — too thin)
   - 2S4P (50F) at 15W → 33.5s (68% margin) — user approved upgrade to 2S4P
   - DEC-029 completely rewritten: 2S4P, 8 cells, 50F, 15W load, ≥33.5s, ≥20s rule
   - DEC-029 includes sensitivity table, correct load warning block, footprint (41×81mm)

5. **User asked about DEC-021 typo ("DEC-0293")** — confirmed should reference DEC-029, not DEC-0293

6. **User asked to verify hold-time calculations**
   - Confirmed at 15W (5V × 3A): boost model (V_lo=2.0V, η=80%) → 629J × 0.80 = 503J → 33.5s ✓
   - Pure-buck model (V_lo=4.75V): 164.9J → 11.0s ❌ — confirms boost converter essential
   - Minimum efficiency to pass 20s: ~48% (far below any credible operating point)
   - User asked to add CM5 load clarification to DEC-029 — done in DEC-029 text

7. **User asked whether R14, eFuse, or LDO need changes at 15W load**
   - Analysis: 5V_MAIN bulk capacitance = C9(22µF) + C10(22µF) + C13(10µF) = **54µF total**
   - Backup threshold (R14=28.7kΩ) = 4.644V; PWR_GD deassert = 4.50V; gap = 144mV
   - At 3A: time before PWR_GD deasserts = 54µF × 144mV / 3A = **2.59µs**
   - LTC3350 default frequency (RT=INTVCC) = 200kHz → 5µs/cycle → **only 0.52 cycles — FAILS**
   - eFuse: no change needed (HV input side)
   - LDO (TPS75733): no change needed (stays in regulation)
   - MIC1555/R28/C32: no change needed (3.01s timing correct)
   - **R14 must be raised** and **bulk capacitance added** OR frequency increased

8. **User asked about C35 capacitor type and spec**
   - Discussed ceramic vs aluminium polymer vs tantalum — ceramic X7R recommended (project standard, lowest ESR)
   - User noted Murata parts are banned from BOM
   - Confirmed no 100µF cap exists anywhere in design (largest is 22µF)
   - User found TDK CKG57NX7R1E107M500JJ (100µF 25V X7R 2220) — confirmed technically suitable
   - User rejected it (looks like stacked caps, ~£9 each)

9. **Revised solution proposed: no exotic 100µF cap needed**
   - Use R30 (new LTC3350 RT resistor ~33.2kΩ) to set LTC3350 to 400kHz
   - Change R14 to 30.1kΩ (threshold 4.812V, gap = 312mV)
   - C35: 2× Samsung CL32B226KAJNNNE (22µF 25V X7R 1210, already in BOM) in parallel = 44µF
   - Combined result: t = 98µF × 312mV / 3A = 10.2µs = 4.1 cycles at 400kHz ✓

10. **User suggested HZA107M025X16T-F** — datasheet downloaded but PDF binary, unable to extract text. Session compacted before resolution.

</history>

<work_done>

Files modified and committed (commit `acae80d`):
- `design/Electronics/Extension/Design_Spec.md` — §5 "Passive components only" root cause fixed; U1 NEVER REMOVE warning added
- `design/Electronics/Power_Module/Design_Spec.md` — eFuse variant lock + supercap cell lock blocks in BOM notes; DR-PM-07/09 updated to 25F/37.5F
- `design/Electronics/Power_Module/Board_Layout.md` — 22F/33F → 25F/37.5F
- `design/Electronics/Boards_Overview.md` — 33F/21.7s → 37.5F/24.8s
- `design/Guides/User_Manual.md` — 22F/33F/21.7s → 25F/37.5F/24.8s
- `design/Software/Linux_OS/Power_Management.md` — ≥21.7s → ≥24.8s
- `design/Standards/Certification_Evidence.md` — ≥21.7s → ≥24.8s
- `design/Design_Log.md` — DEC-004/021 superseded; DEC-029 created (rewritten to 2S4P/15W)

**DEC-029 already updated to 2S4P/15W in Design_Log.md but NOT yet cascaded to other files.**

Work completed:
- [x] eFuse variant lock blocks added
- [x] Extension U1 root cause fixed
- [x] Supercap stale value sweep (22F/33F → 25F/37.5F)
- [x] DEC-004 and DEC-021 marked superseded
- [x] DEC-029 created and rewritten to 2S4P/50F/15W/33.5s
- [x] Transient margin analysis at 3A load (R14/C35/R30 fix identified)
- [x] C35 component selection resolved (2× existing BOM 22µF 25V X7R 1210)
- [ ] **2S4P cascade to all files — NOT YET DONE**
- [ ] **R14 change (28.7kΩ → 30.1kΩ), R30 addition (33.2kΩ), C35 addition (2× 22µF)**
- [ ] **DEC-030 creation (transient analysis and R14/R30/C35 fix)**
- [ ] **HZA107M025X16T-F datasheet review (PDF unreadable, user question pending)**
- [ ] markdownlint run, commit, checkpoint 029

</work_done>

<technical_details>

**eFuse variant lock (permanent):**
- TPS259804ONRGER = CORRECT (16.9V silicon-fixed OVLO, cut-tape)
- TPS259807 = WRONG (no OVLO), TPS259803 = WRONG (no OVLO)
- "04" digit in MPN selects OVLO variant; "ONRGER" = cut-tape (same silicon as ONRGE)
- Variant lock blocks in DEC-005 and PM/Design_Spec.md BOM notes

**Supercap — definitive configuration:**
- Cell: Abracon ADCR-T02R7SA256MB, 25F/2.7V each
- Configuration: **2S4P — 8 cells** (C_SC1–C_SC8)
- Effective: **50F at 5.4V**
- Block footprint: **37mm × 77mm**; shadow zone: **41mm × 81mm**
- Charge time from depleted at 0.5A: **~9 minutes** (previous "~3 min" was wrong)
- Load for hold-up calculation: **15W** (CM5 draws 5V × 3A typical — NOT 5W)
- Hold-up: **33.5s** (boost model, V_lo=2.0V, η=80%, E=503J)
- Minimum efficiency to pass 20s rule: ~48%

**DEC status:**
- DEC-004: Superseded by DEC-029 (0.5A charge current constraint retained)
- DEC-021: Superseded by DEC-029 (2S4P upgrade documented)
- DEC-029: Authoritative — 2S4P, 8 cells, 50F, 15W, ≥33.5s, ≥20s rule

**Stale values — must NEVER reappear:**
- 22F cells, 33F bank, 21.7s (pre-Abracon)
- 37.5F, 24.8s, 2S3P, 6 cells, C_SC1–6 (post-Abracon, pre-2S4P)
- 5W as hold-up design load; "~3 minutes" charge time
- "Passive components only" for Extension Design_Spec §5

**5V_MAIN backup transient analysis:**
- 5V_MAIN bulk C on PM board: C9(22µF) + C10(22µF) + C13(10µF) = **54µF**
- At 3A load, time before PWR_GD (4.50V) deasserts: 54µF × 144mV / 3A = **2.59µs**
- LTC3350 default (RT=INTVCC): 200kHz = 5µs/cycle → **FAILS** (0.52 cycles)
- Fix: R14 → 30.1kΩ (threshold 4.812V, gap 312mV) + R30 33.2kΩ (400kHz) + C35 (2× 22µF)
- With fix: 98µF × 312mV / 3A = 10.2µs = **4.1 cycles at 400kHz ✓**
- False-trigger headroom: 4.90V (5V×0.98) − 4.812V = 88mV (LTC3350 ~12µs deglitch filters brief dips)

**LTC3350 RT pin frequency setting:**
- RT=INTVCC (default, no resistor) = 200kHz
- RT resistor to GND sets higher frequency: ~33.2kΩ → 400kHz
- No RT resistor currently in BOM — this is an omission that needs fixing

**Murata ban:** All Murata parts (GRM, GCM, etc.) are banned from BOM. Only historical note remains in PM/Design_Spec.md BOM notes (describing the superseded original spec).

**Project ceramic capacitor rule:** All ceramics must use X7R dielectric. X7S was asked about — technically acceptable but violates project rule.

**HZA107M025X16T-F:** User proposed this as C35. Datasheet downloaded as `design/Datasheets/HZA-datasheet.pdf`. PDF is binary-encoded, could not extract text. Part number suggests: 100µF, ±20%, 25V, "X16" likely package size code. Type unknown — could be aluminium polymer hybrid. Needs verification before acceptance.

**Agreed C35 solution (before HZA question):** 2× Samsung CL32B226KAJNNNE (22µF 25V X7R 1210, existing BOM part) in parallel — no new part number needed, 25V rating gives excellent derating at 5V operating.

</technical_details>

<important_files>

- `design/Design_Log.md`
  - Contains DEC-004 (Superseded), DEC-021 (Superseded), DEC-029 (authoritative supercap spec, 2S4P/15W/50F/33.5s)
  - DEC-029 already updated to 2S4P — this is the reference; all other files must match it
  - DEC-030 (backup transient fix: R14/R30/C35) still needs to be created here

- `design/Electronics/Power_Module/Design_Spec.md`
  - Primary PM spec — still shows 2S3P/37.5F/24.8s/5W/6-cell throughout; ALL must cascade to 2S4P/50F/33.5s/15W/8-cell
  - DR-PM-08 (R14): still shows 28.7kΩ/4.644V — must update to 30.1kΩ/4.812V
  - DR-PM-10 (new): C35 dedicated 5V_MAIN bulk cap needs adding
  - BOM: R14 MPN change, R30 new entry (33.2kΩ RT resistor), C35 new entry (2× 22µF in parallel)
  - BOM Notes supercap lock block: must update from 2S3P to 2S4P

- `design/Electronics/Power_Module/Board_Layout.md`
  - ASCII supercap grid still shows 2×3 (6 cells) — needs 2×4 (8 cells), shadow zone 41×61→41×81
  - Power chain still shows 37.5F — needs 50F

- `design/Guides/User_Manual.md`
  - §3.6: 6 cells/37.5F/24.8s/3 min → 8 cells/50F/33.5s/9 min

- `design/Software/Linux_OS/Power_Management.md`
  - Timeline table: ≥24.8s → ≥33.5s (×2)

- `design/Electronics/Boards_Overview.md`
  - PM description: 37.5F/6×/2S3P/24.8s → 50F/8×/2S4P/33.5s

- `design/Standards/Certification_Evidence.md`
  - ≥24.8 seconds → ≥33.5 seconds

- `design/Electronics/Consolidated_BOM.md`
  - C_SC row: Qty 6 → 8; add C35, R30 as new line items

- `design/Datasheets/HZA-datasheet.pdf`
  - User-provided datasheet for HZA107M025X16T-F capacitor (proposed C35 alternative)
  - PDF is binary-encoded — cannot be read with text tools; needs proper PDF reader or user to provide specs

- `.copilot/agent-prompts/r52-review-prompt.txt`
  - Stale values list needs updating: add 37.5F/24.8s/2S3P/6-cell/5W/C_SC1–6/3-min-charge as stale; add correct values

</important_files>

<next_steps>

**Immediate blocker — resolve HZA107M025X16T-F:**
- The user asked about this part as an alternative for C35
- Datasheet is at `design/Datasheets/HZA-datasheet.pdf` but PDF is unreadable as text
- Need to determine: is it ceramic X7R, aluminium polymer, or other type? What is actual ESR?
- If suitable: use as C35 (single component), get distributor PNs from user
- If not suitable: fall back to agreed solution (2× Samsung CL32B226KAJNNNE in parallel + R30)

**Once C35 is confirmed, implement all pending changes in one commit:**

1. `design/Design_Log.md` — Create DEC-030 (backup transient analysis: 54µF bulk, 2.59µs window at 3A FAILS, fix: R14→30.1kΩ + R30 33.2kΩ + C35; with fix: 10.2µs/4.1 cycles at 400kHz)
2. `design/Electronics/Power_Module/Design_Spec.md` — Full 2S4P cascade (FR-PM-02/07, DR-PM-07/09, §1/§2/§3, BOM lock block, BOM table); update DR-PM-08 (R14: 28.7k→30.1k, threshold 4.644V→4.812V); add DR-PM-10 (C35); add R30 and C35 to BOM table; update R14 MPN
3. `design/Electronics/Power_Module/Board_Layout.md` — ASCII 2×3→2×4, labels, shadow zone 41×61→41×81, power chain 37.5F→50F
4. `design/Guides/User_Manual.md` — 6→8 cells, 37.5F→50F, 24.8s→33.5s, 3 min→9 min
5. `design/Software/Linux_OS/Power_Management.md` — ≥24.8s→≥33.5s (×2)
6. `design/Electronics/Boards_Overview.md` — 37.5F/6×/2S3P/24.8s→50F/8×/2S4P/33.5s
7. `design/Standards/Certification_Evidence.md` — ≥24.8s→≥33.5s
8. `design/Electronics/Consolidated_BOM.md` — C_SC qty 6→8; add C35 and R30 rows
9. `.copilot/plan.md` — add stale values: 37.5F/24.8s/2S3P/6-cell/C_SC1–6/5W/3-min-charge
10. `.copilot/agent-prompts/r52-review-prompt.txt` — same stale values update
11. Run `markdownlint --fix "design/**/*.md"` then clean check
12. Commit with Co-authored-by trailer
13. Create checkpoint 029

**After all above: user has a new feature idea to discuss (held until PM transient work is fully committed)**

</next_steps>