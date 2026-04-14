<overview>
This session segment focused on resolving the root causes of recurring design regressions in Enigma-NG Power Module documentation (eFuse MPN swapping, supercap values reverting, Extension U1 buffer removal), upgrading the supercap bank from 2S3P to 2S4P after correcting the load assumption from 5W to 15W (CM5 at 5V×3A), and resolving a newly discovered transient margin failure on 5V_MAIN during LTC3350 backup switchover. A combined 3-part fix was designed (R14 + R30 + C35), with C35 confirmed as 2× Samsung CL32B226KAJNNNE (22µF 25V X7R 1210) after evaluating and rejecting HZA107M025X16T-F (marginal at −40°C) and T495X107K025ATA150 (ESR too high — FAILS). The full cascade of 2S4P and transient fix changes across all design documents is pending implementation.
</overview>

<history>

1. **User asked why eFuse MPN (TPS259804 ↔ TPS259807) keeps changing**
   - Confirmed TPS259804ONRGER = correct (16.9V silicon-fixed OVLO, cut-tape)
   - TPS259807/TPS259803 = wrong (no OVLO)
   - Added `⚠️ eFuse variant lock` block to PM/Design_Spec.md BOM notes and DEC-005
   - Added Part Number Change Rule: datasheet must exist in `design/Datasheets/` before any MPN change

2. **User asked about root causes of Extension U1 removal and supercap stale values**
   - Extension root cause: §5 said "Passive components only" → review agents removed U1 (SN74LVC2G125DCUR). Fixed with explicit "U1 is the only active IC" + NEVER REMOVE warning
   - Supercap root cause: PM/Design_Spec.md had correct Abracon 25F but 6 other docs had stale 22F/33F/21.7s → agents "corrected" PM back to match majority. Fixed by sweeping all files to 25F/37.5F/24.8s

3. **User asked to create DEC-029 as authoritative supercap spec, obsolete DEC-004 and DEC-021**
   - DEC-004 marked Superseded by DEC-029 (0.5A charge current retained)
   - DEC-021 marked Superseded by DEC-029 (initially created as 2S3P/5W)
   - User corrected: DEC-021 had a typo "DEC-0293" — should reference DEC-029. Fixed.

4. **User corrected load assumption: CM5 draws 5V × 3A = 15W (not 5W)**
   - Recalculated: 2S3P (37.5F) at 15W → 25.2s (only 26% margin — too thin)
   - 2S4P (50F) at 15W → 33.5s (68% margin) — user approved 2S4P upgrade
   - DEC-029 fully rewritten: 2S4P, 8 cells, 50F, 15W load, ≥33.5s, ≥20s rule, sensitivity table, footprint (41×81mm)
   - Calculations confirmed: boost model (V_lo=2.0V, η=80%), E=629J×0.80=503J → 33.5s ✓

5. **User asked to add CM5 3A load clarification to DEC-029** — done.

6. **User asked whether R14, eFuse, or LDO need changes at 15W load**
   - Analysis: 5V_MAIN bulk C = C9(22µF)+C10(22µF)+C13(10µF) = 54µF total
   - Backup threshold (old R14=28.7kΩ) = 4.644V; PWR_GD deassert = 4.50V; gap = 144mV
   - At 3A: time before PWR_GD trips = 54µF × 144mV / 3A = **2.59µs**
   - LTC3350 default at 200kHz → 5µs/cycle → **0.52 cycles — FAILS**
   - eFuse: no change needed; LDO (TPS75733): no change; MIC1555/R28/C32: no change
   - Combined fix designed: R14→30.1kΩ (threshold 4.812V, 312mV gap) + R30=33.2kΩ (LTC3350 400kHz) + C35 (bulk cap)

7. **User asked about cap type for C35 — extensive search conducted**
   - Ceramics: no 100µF X7R in existing BOM; project bans Murata; TDK CKG57NX7R1E107M500JJ (100µF 25V X7R 2220) was found but rejected by user (looks like stacked plates, ~£9 each)
   - **Revised solution**: all 3 changes together only need 44µF, not 100µF — 2× existing BOM Samsung CL32B226KAJNNNE (22µF 25V X7R 1210) in parallel = 44µF
   - Result: 98µF × 312mV / 3A = 10.2µs = **4.1 cycles at 400kHz ✓**

8. **User suggested HZA107M025X16T-F (Cornell Dubilier)**
   - Datasheet extracted via pdfplumber: Hybrid Polymer-Aluminum SMD, 6.3×7.7mm, AEC-Q200
   - ESR = **30mΩ max at 100kHz/+20°C** → 4.56 cycles ✓ at +20°C
   - At −40°C: ESR rises ~2× to ~60mΩ → only ~2.1 cycles (marginal)
   - User said "best option so far, keep looking"

9. **User suggested T495X107K025ATA150 (KEMET tantalum)**
   - Datasheet extracted: MnO₂ tantalum, Case X (7.3×4.3×4.0mm), **ESR = 150mΩ max**
   - Analysis: V_ESR = 3A × 0.150Ω = **450mV — exceeds entire 312mV budget by 44%**
   - Additional concern: MnO₂ tantalum fails short-circuit (fire risk in power bypass)
   - **Rejected outright**

10. **User asked why 100µF was specified but 2×22µF (44µF) was also suggested**
    - Clarified: 100µF was the pre-fix estimate (before R14/R30 changes were incorporated). With the combined 3-part fix, only 44µF is needed. The solution evolved from "just add a big cap" to "3 changes working together."

11. **User confirmed: use 2× Samsung CL32B226KAJNNNE as C35** (combined fix accepted)

12. **User asked to remove unwanted datasheets**
    - Removed: `HZA-datasheet.pdf` and `KEM_T2052_T495_AUTO-datasheet.pdf`
    - Both were NOT tracked by git (confirmed) — no commit impact

</history>

<work_done>

Files modified and committed (commit `acae80d`):
- `design/Electronics/Extension/Design_Spec.md` — §5 root cause fixed; U1 NEVER REMOVE warning
- `design/Electronics/Power_Module/Design_Spec.md` — eFuse lock + supercap cell lock blocks; DR-PM-07/09 updated to 25F/37.5F
- `design/Electronics/Power_Module/Board_Layout.md` — 22F/33F → 25F/37.5F
- `design/Electronics/Boards_Overview.md` — 33F/21.7s → 37.5F/24.8s
- `design/Guides/User_Manual.md` — 22F/33F/21.7s → 25F/37.5F/24.8s
- `design/Software/Linux_OS/Power_Management.md` — ≥21.7s → ≥24.8s
- `design/Standards/Certification_Evidence.md` — ≥21.7s → ≥24.8s
- `design/Design_Log.md` — DEC-004/021 superseded; DEC-029 created (rewritten to 2S4P/15W/50F/33.5s)

Files deleted (not git-tracked):
- `design/Datasheets/HZA-datasheet.pdf` — deleted
- `design/Datasheets/KEM_T2052_T495_AUTO-datasheet.pdf` — deleted

Current git status: `design/Design_Log.md` is modified but **not yet committed** (DEC-029 2S4P rewrite from session).

Work completed:
- [x] eFuse variant lock blocks added to PM/Design_Spec.md and DEC-005
- [x] Extension U1 root cause fixed
- [x] Supercap stale value sweep (22F/33F → 25F/37.5F across all files)
- [x] DEC-004 and DEC-021 marked superseded
- [x] DEC-029 created and rewritten to 2S4P/50F/15W/33.5s
- [x] 5V_MAIN backup transient analysis complete (R14/R30/C35 fix designed)
- [x] C35 component confirmed: 2× Samsung CL32B226KAJNNNE (22µF 25V X7R 1210)
- [x] HZA107M025X16T-F evaluated and not selected
- [x] T495X107K025ATA150 evaluated and rejected
- [x] Unwanted datasheets removed

**Still pending (no changes made yet):**
- [ ] 2S4P cascade to all files (PM/Design_Spec.md, Board_Layout.md, User_Manual.md, Power_Management.md, Boards_Overview.md, Certification_Evidence.md, Consolidated_BOM.md)
- [ ] R14 change (28.7kΩ → 30.1kΩ) in PM/Design_Spec.md DR-PM-08
- [ ] R30 new entry (33.2kΩ RT resistor) in PM/Design_Spec.md and BOM
- [ ] C35 new entry (2× Samsung CL32B226KAJNNNE) in PM/Design_Spec.md and BOM
- [ ] DR-PM-10 creation (C35 dedicated 5V_MAIN bulk)
- [ ] DEC-030 creation (backup transient analysis and fix)
- [ ] markdownlint fix/check cycle
- [ ] Git commit with Co-authored-by trailer
- [ ] Checkpoint 031

</work_done>

<technical_details>

**eFuse variant lock (permanent):**
- TPS259804ONRGER = CORRECT (16.9V silicon-fixed OVLO, cut-tape)
- TPS259807 = WRONG (no OVLO), TPS259803 = WRONG (no OVLO)
- "04" digit selects OVLO variant; "ONRGER" = cut-tape (same silicon as ONRGE)

**Supercap — definitive configuration:**
- Cell: Abracon ADCR-T02R7SA256MB, 25F/2.7V each
- Configuration: **2S4P — 8 cells** (C_SC1–C_SC8)
- Effective: **50F at 5.4V**
- Block footprint: **37mm × 77mm**; shadow zone: **41mm × 81mm**
- Charge time from depleted at 0.5A: **~9 minutes**
- Design load: **15W** (CM5 at 5V × 3A — NOT 5W)
- Hold-up: **≥33.5s** (boost model, V_lo=2.0V, η=80%, E=503J)
- Rule: ≥20s minimum

**DEC status:**
- DEC-004: Superseded by DEC-029
- DEC-021: Superseded by DEC-029
- DEC-029: Authoritative — 2S4P, 8 cells, 50F, 15W, ≥33.5s, ≥20s rule
- DEC-030: Pending creation — backup transient fix

**5V_MAIN backup transient fix (3-part combined):**
- Existing 5V_MAIN bulk: C9(22µF) + C10(22µF) + C13(10µF) = 54µF
- Old state: 54µF × 144mV / 3A = 2.59µs = 0.52 cycles at 200kHz → FAILS
- R14: 28.7kΩ → **30.1kΩ** → backup threshold 4.644V → 4.812V → gap 144mV → **312mV**
- R30: **33.2kΩ** to GND on LTC3350 RT pin → sets switching frequency to **400kHz** (2.5µs/cycle)
  - Note: no R30 exists in current BOM — this is an omission that needs adding
  - RT=INTVCC (no resistor) = 200kHz default; resistor to GND increases frequency
- C35: 2× **Samsung CL32B226KAJNNNE** (22µF 25V X7R 1210) in parallel = 44µF added
  - Part already in BOM — no new MPN needed
- With fix: total 98µF × 312mV / 3A = **10.2µs = 4.1 cycles at 400kHz ✓**
- False-trigger headroom: 5V×0.98=4.90V − 4.812V = 88mV (LTC3350 ~12µs deglitch protects against brief dips)

**Capacitor technology comparison for C35:**
- Samsung CL32B226K (X7R ceramic): ~10mΩ ESR, temperature-stable, existing BOM, 44µF total → 4.1 cycles ✓
- HZA107M025X16T-F (CDE Hybrid Polymer-Al): 30mΩ max ESR, 100µF, 4.56 cycles at +20°C, but ~2.1 cycles at −40°C (marginal) — not selected
- T495X107K025ATA150 (KEMET MnO₂ tantalum): 150mΩ ESR → 450mV drop at 3A exceeds 312mV budget → FAILS; also short-circuit failure mode risk — rejected

**Stale values — must NEVER reappear in any document:**
- 22F cells, 33F bank, 21.7s (pre-Abracon values)
- 37.5F, 24.8s, 2S3P, 6 cells, C_SC1–6 (post-Abracon, pre-2S4P — ALL stale)
- 5W as hold-up design load; "~3 minutes" charge time
- "Passive components only" for Extension Design_Spec §5
- R14=28.7kΩ and threshold 4.644V (pre-fix values)
- TPS259807 or TPS259803 as eFuse MPN

**pdfplumber usage:** Python 3.11.5 is available via `$env:PATH` refresh. `python -m pip install pdfplumber` works. Used to extract text from CDE HZA and KEMET T495 datasheets.

**Git note:** `design/Datasheets/` PDF files are tracked by git. The HZA and T495 datasheets were NOT in git (confirmed with `git ls-files`), so deleting them left no git change. The Design_Log.md modification (DEC-029 2S4P rewrite) is staged but uncommitted.

</technical_details>

<important_files>

- `design/Design_Log.md`
  - Contains DEC-004 (Superseded), DEC-021 (Superseded), DEC-029 (authoritative — 2S4P/15W/50F/33.5s)
  - **Modified but not yet committed** — DEC-029 2S4P rewrite is the reference for all cascade changes
  - DEC-030 (backup transient fix: R14/R30/C35) needs to be added here

- `design/Electronics/Power_Module/Design_Spec.md`
  - Primary PM spec — **still shows 2S3P/37.5F/24.8s/5W/6-cell throughout** — ALL must cascade to 2S4P/50F/33.5s/15W/8-cell
  - DR-PM-08 (R14): still shows 28.7kΩ/4.644V — must update to 30.1kΩ/4.812V
  - DR-PM-10 (new): C35 dedicated 5V_MAIN bulk cap needs adding
  - BOM: R14 MPN update; R30 new entry (33.2kΩ RT resistor); C35 new entry (2× 22µF Samsung)
  - BOM Notes supercap lock block: must update from 2S3P to 2S4P

- `design/Electronics/Power_Module/Board_Layout.md`
  - ASCII supercap grid still shows 2×3 (6 cells) — needs 2×4 (8 cells)
  - Shadow zone: 41×61 → **41×81mm**

- `design/Guides/User_Manual.md`
  - §3.6: 6 cells/37.5F/24.8s/3 min → 8 cells/50F/33.5s/**9 min**

- `design/Software/Linux_OS/Power_Management.md`
  - Timeline table: ≥24.8s → **≥33.5s** (×2 occurrences)

- `design/Electronics/Boards_Overview.md`
  - PM description: 37.5F/6×/2S3P/24.8s → **50F/8×/2S4P/33.5s**

- `design/Standards/Certification_Evidence.md`
  - ≥24.8 seconds → **≥33.5 seconds**

- `design/Electronics/Consolidated_BOM.md`
  - C_SC row: Qty 6 → **8**; add C35 (2× Samsung CL32B226KAJNNNE), R30 (33.2kΩ) as new line items

</important_files>

<next_steps>

Confirmed fix (implement all in one pass):
- **C35 = 2× Samsung CL32B226KAJNNNE** (22µF 25V X7R 1210, existing BOM part) in parallel = 44µF
- **R14 = 30.1kΩ** (was 28.7kΩ), threshold 4.812V
- **R30 = 33.2kΩ** (new, LTC3350 RT pin to GND, sets 400kHz)
- Combined result: 98µF × 312mV / 3A = 10.2µs = 4.1 cycles ✓

Implementation order:
1. `design/Design_Log.md` — Create DEC-030 (full transient analysis: old state FAILS, fix rationale, all three changes, result)
2. `design/Electronics/Power_Module/Design_Spec.md` — Full 2S4P cascade (FR-PM-02/07, DR-PM-07/09, §1/§2/§3, BOM lock block, BOM table); DR-PM-08 R14 update; add DR-PM-10; add R30 + C35 to BOM
3. `design/Electronics/Power_Module/Board_Layout.md` — ASCII 2×3→2×4, shadow zone 41×61→41×81, power chain 37.5F→50F
4. `design/Guides/User_Manual.md` — 6→8 cells, 37.5F→50F, 24.8s→33.5s, 3 min→9 min
5. `design/Software/Linux_OS/Power_Management.md` — ≥24.8s→≥33.5s (×2)
6. `design/Electronics/Boards_Overview.md` — 37.5F/6×/2S3P/24.8s→50F/8×/2S4P/33.5s
7. `design/Standards/Certification_Evidence.md` — ≥24.8s→≥33.5s
8. `design/Electronics/Consolidated_BOM.md` — C_SC qty 6→8; add C35 and R30 rows
9. Run `markdownlint --fix "design/**/*.md"` then clean check
10. Git commit with Co-authored-by trailer
11. Create checkpoint 031

**After commit: User has a new feature idea to discuss (held pending completion of PM transient work)**

Blockers: None — all decisions confirmed.

</next_steps>