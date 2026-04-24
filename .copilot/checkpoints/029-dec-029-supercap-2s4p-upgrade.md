<overview>
This session focused on diagnosing and permanently fixing three recurring regressions in the Enigma-NG design documentation that had survived multiple review cycles: the eFuse MPN being swapped to an incorrect variant, the Extension board U1 JTAG buffer being repeatedly removed, and supercap values reverting to pre-Abracon stale figures. The approach was to identify root causes in the design documentation itself (contradictory, missing, or ambiguous text), fix those root causes with explicit lock notes, add a new authoritative Design Decision (DEC-029) for the supercap hold-up specification, and discovered mid-session that the load assumption (5W) was incorrect — it should be 15W (5V × 3A CM5 typical) — which also triggered an upgrade from 2S3P (6 cells) to 2S4P (8 cells) for adequate margin.
</overview>

<history>

1. **User asked for a summary of the session reviews before continuing**
   - Agent confirmed clean state from prior session (commit `77ea120`), J_INT 4-header redesign and POS_B naming complete, all connector MPNs confirmed
2. **User asked why the eFuse MPN keeps changing (TPS259804 ↔ TPS259807)**
   - Agent found live docs already correctly show TPS259804ONRGER; the confusion was in stale session memories
   - Added `⚠️ eFuse variant lock` block to PM/Design_Spec.md BOM notes and Design_Log DEC-005 with comparison table (04=correct 16.9V OVLO, 07=wrong no OVLO, 03=wrong no OVLO)
   - Added "Part Number Change Rule" to plan.md and r52-review-prompt.txt: datasheet must exist in `design/Datasheets/` before any MPN change
3. **User confirmed eFuse MPN is TPS259804ONRGER (cut-tape, with R suffix)**
   - Session had briefly changed to ONRGE (without R), then user confirmed ONRGER is correct
   - Reverted and confirmed ONRGER throughout all files; variant lock notes retained
4. **User asked to investigate supercap stale values and Extension U1 removal root causes**

   **Extension U1 root cause found:**
   - `Extension/Design_Spec.md §5` contained "Passive components only." — review agents read this as "no active components on this board" and flagged/removed U1
   - Fixed: replaced with explicit statement that U1 (SN74LVC2G125DCUR) is the only active IC, <10mW, no heatsinking, plus `⚠️ U1 must never be removed` warning referencing FR-EXT-01/02, DR-EXT-04/05/06

   **Supercap stale values root cause found:**
   - Checkpoint 025 (Abracon selection) updated PM/Design_Spec.md but left stale 22F/33F/21.7s in 6 other files
   - Review agents found the majority of docs saying 22F/33F and "corrected" PM/Design_Spec back to match
   - Stale value sweep: updated User_Manual, Power_Management, Boards_Overview, Certification_Evidence, PM/Board_Layout, Design_Log DEC-004
5. **User confirmed 2S3P configuration and asked to add supercap lock notes**
   - Added `⚠️ Supercap cell lock` block to PM/Design_Spec.md BOM notes (25F/37.5F/24.8s)
   - Added post-decision note to DEC-021 recording the Abracon upgrade from 22F to 25F
   - Added 22F/33F/21.7s to Stale Values in plan.md and r52-review-prompt.txt
   - Added "Passive components only" Extension §5 to Stale Values list
6. **User asked to create DEC-029 as the authoritative supercap hold-up spec, obsolete DEC-004 and DEC-021**
   - DEC-004 marked: `Superseded by DEC-029` (0.5A charge current constraint retained)
   - DEC-021 marked: `Superseded by DEC-029` (2S3P arrangement retained; cell cap upgraded)
   - DEC-029 created with 2S3P, 5W load, conservative and realistic hold-up models
   - Committed `acae80d`, checkpoint 028 created
7. **User pointed out 5W load is wrong — CM5 draws 3A minimum at 5V = 15W**
   - Agent recalculated: at 15W, 2S3P (37.5F) conservative (pure-buck) = 8.2s ❌ FAILS
   - Realistic (boost to 2.0V, 80% eff): 25.2s ✅ — passes but only 26% margin
   - 2S4P (50F) at 15W: 33.5s ✅ — 68% margin; user selected upgrade to 2S4P
8. **User asked to update DEC-029 with the 15W load clarification and 2S4P configuration**
   - DEC-029 completely rewritten with: 2S4P (8 cells, 50F), 15W load, explicit "correct load figure" warning block, full sensitivity table (48% min efficiency still passes), updated footprint (41×81mm shadow zone), charge time ~9 min
   - **This edit is committed to Design_Log.md only — cascade to all other docs is IN PROGRESS, not yet done**

</history>

<work_done>

Files modified and committed this session (commit `acae80d` — all changes up to DEC-029 initial creation):
- `design/Electronics/Extension/Design_Spec.md` — §5 "Passive components only" root cause fixed
- `design/Electronics/Power_Module/Design_Spec.md` — eFuse variant lock + supercap cell lock blocks added to BOM notes; DR-PM-07/09 stale values updated
- `design/Electronics/Power_Module/Board_Layout.md` — 22F/33F → 25F/37.5F in ASCII and power chain
- `design/Electronics/Boards_Overview.md` — 33F/21.7s → 37.5F/24.8s
- `design/Guides/User_Manual.md` — 22F/33F/21.7s → 25F/37.5F/24.8s
- `design/Software/Linux_OS/Power_Management.md` — ≥21.7s → ≥24.8s (×2)
- `design/Standards/Certification_Evidence.md` — ≥21.7s → ≥24.8s
- `design/Design_Log.md` — DEC-004/021 superseded; DEC-021 post-note; DEC-004 cell ref fixed; DEC-029 created (initially 2S3P/5W — now superseded by rewrite)
- `.copilot/plan.md` — Part Number Change Rule + stale values updated
- `.copilot/agent-prompts/r52-review-prompt.txt` — same updates
- `.copilot/checkpoints/028-dec029-supercap-efuse-root-causes.md` — checkpoint created

**Most recent edit (NOT yet committed, NOT yet cascaded):**
- `design/Design_Log.md` DEC-029 — fully rewritten to 2S4P, 15W load, sensitivity table, correct footprint

**PENDING — not yet done (interrupted by compaction request):**

The following files still contain the now-stale 2S3P/37.5F/24.8s values and need updating to 2S4P/50F/33.5s:

- `design/Electronics/Power_Module/Design_Spec.md`:
  - FR-PM-02: "≥24.8 s" → "≥33.5 s", "C_SC1–6" → "C_SC1–8"
  - FR-PM-07: "24.8 s hold-up window" → "33.5 s hold-up window"
  - DR-PM-07: "6× 25F, 2S3P, 37.5F, C_SC1–6" → "8× 25F, 2S4P, 50F, C_SC1–8"
  - DR-PM-09: "≥24.8 s at 5W" → "≥33.5 s at 15W"
  - §1 Supercap Block: "2×3, 6 cells, 37mm×57mm, 41×61mm" → "2×4, 8 cells, 37mm×77mm, 41×81mm"
  - §2 Storage: "6×, 2S3P, 37.5F, 123.8J, 24.8s at 5W" → "8×, 2S4P, 50F, 503J, 33.5s at 15W"
  - §2 Supercap Manager: "6-cell, 2S3P, 37.5F" → "8-cell, 2S4P, 50F"
  - §3 Sequencing step 4: "6-cell, 37.5F, ~3 minutes, 24.8s at 5W" → "8-cell, 50F, ~9 minutes, 33.5s at 15W"
  - §3 Sequencing step 5: "≥24.8 seconds" → "≥33.5 seconds"
  - BOM Notes supercap lock block: "2S3P, 6 cells, 37.5F, 24.8s" → "2S4P, 8 cells, 50F, 33.5s at 15W"
  - BOM table row: "C_SC1–6, 2S3P, 6×" → "C_SC1–8, 2S4P, 8×"
- `design/Electronics/Power_Module/Board_Layout.md`:
  - ASCII diagram: add C_SC7/C_SC8 row (2×3 → 2×4)
  - ASCII diagram label: "37.5F/5.4V, 25F×6 cells, 2S3P" → "50F/5.4V, 25F×8 cells, 2S4P"
  - Power chain: "[C_SC1-6: 37.5F / 5.4V]" → "[C_SC1-8: 50F / 5.4V]"
  - Shadow zone: 41×61mm → 41×81mm
- `design/Guides/User_Manual.md` §3.6: "25F × 6, 37.5F, 24.8s" → "25F × 8, 50F, 33.5s", "3 minutes" → "9 minutes"
- `design/Software/Linux_OS/Power_Management.md`: "≥24.8 s" → "≥33.5 s" (×2)
- `design/Electronics/Boards_Overview.md`: "37.5F (6× Abracon 25F/2.7V, 2S3P), ≥24.8s" → "50F (8× Abracon 25F/2.7V, 2S4P), ≥33.5s"
- `design/Standards/Certification_Evidence.md`: "≥24.8 seconds" → "≥33.5 seconds"
- `design/Electronics/Consolidated_BOM.md`: C_SC count 6 → 8
- `.copilot/plan.md`: add "37.5F, 24.8s, 2S3P" to stale values; add 50F/33.5s/2S4P as correct
- `.copilot/agent-prompts/r52-review-prompt.txt`: same stale values update

After all edits: run markdownlint, commit, create checkpoint 029.

</work_done>

<technical_details>

**eFuse variant lock (permanent):**
- TPS259804ONRGER = CORRECT (16.9V silicon-fixed OVLO, cut-tape orderable MPN)
- TPS259807 = WRONG (no OVLO), TPS259803 = WRONG (no OVLO)
- OVLO 16.9V matches 4S battery max charge 4.1V/cell = 16.4V, 0.5V margin
- "04" digit in MPN selects OVLO variant; "ONRGER" = cut-tape packaging (same silicon as ONRGE)
- Variant lock blocks in DEC-005 and PM/Design_Spec.md BOM notes

**Extension U1 buffer root cause (fixed):**
- The phrase "Passive components only." in §5 Thermal caused review agents to flag U1 as anomalous
- Fix: explicit "U1 is the only active IC, <10mW" statement + NEVER REMOVE warning
- U1 = SN74LVC2G125DCUR (VSSOP-8), buffers TCK and TMS for every 5-rotor group
- C6 = 0.1µF X7R 0402 local bypass for U1 VCC

**Supercap configuration — definitive:**
- Cell: Abracon ADCR-T02R7SA256MB, 25F/2.7V each (confirmed in-stock)
- Configuration: **2S4P — 8 cells** (C_SC1–C_SC8)
- Effective: **50F at 5.4V** (4 parallel per series position × 2 in series)
- Block footprint: **37mm × 77mm** (2 cols × 4 rows at 20mm pitch, 16.5mm max dia)
- Shadow zone (PCB no-fly zone): **41mm × 81mm**
- Charge time from depleted at 0.5A: **~9 minutes** (100F/position × 2.7V / 0.5A = 540s)
- Note: previous docs all said "~3 minutes" — this was an error from the original calc

**Supercap hold-up calculation — definitive:**
- Load: **15W** (CM5 draws 5V × 3A typical; this is the design load for shutdown hold-up)
- Formula: E = ½ × C × (V_hi² − V_lo²), then t = E × η / P
- Pure-buck model (V_lo=4.75V, no boost): 164.9J → **11.0s ❌** — confirms boost is essential
- Realistic model (V_lo=2.0V, η=80%): 629J × 0.80 = 503J → **33.5s ✅**
- Minimum efficiency to pass 20s: ~48% (far below any credible operating point)
- Previous 5W load figure was wrong — the OS shutdown runs at near-full CM5 load
- Previous "24.8s" and "37.5F" values are now stale (replaced by 33.5s and 50F)
- 2S3P at 15W: only 25.2s (26% margin) — reason for upgrade to 2S4P
- 2S4P at 15W: 33.5s (68% margin) — adequate headroom for aging and efficiency variation

**DEC status:**
- DEC-004: Superseded by DEC-029 (0.5A PoE charge current constraint still valid and retained)
- DEC-021: Superseded by DEC-029 (2S3P→2S4P upgrade documented in DEC-029)
- DEC-029: Authoritative hold-up spec — 2S4P, 8 cells, 50F, 15W load, ≥33.5s, ≥20s rule

**Stale values that must never reappear:**
- 22F cells, 33F bank, 21.7s (pre-Abracon)
- 37.5F, 24.8s, 2S3P, 6 cells, C_SC1–6 (post-Abracon but pre-2S4P upgrade)
- 5W as the hold-up design load
- "~3 minutes" charge time (correct is ~9 minutes for 2S4P)
- "Passive components only" for Extension Design_Spec §5

**Review process improvements (permanent):**
- Part Number Change Rule in plan.md + r52-review-prompt.txt: datasheet must exist in `design/Datasheets/`, key parameters verified before any MPN change
- DEC-029 contains explicit cell lock warning and correct load figure to prevent future regression

</technical_details>

<important_files>

- `design/Design_Log.md`
  - Contains DEC-004 (Superseded), DEC-021 (Superseded), and DEC-029 (new authoritative supercap spec)
  - DEC-029 is the most recently edited section (~line 1210+); **already updated to 2S4P/15W**
  - DEC-029 includes: configuration table, correct load explanation, conservative + realistic models, sensitivity table, rationale, constraints
  - DEC-005 eFuse variant lock block also present
- `design/Electronics/Power_Module/Design_Spec.md`
  - Primary PM spec; contains FR-PM-02/07, DR-PM-07/09, §1 supercap block, §2 storage, §3 sequencing, BOM lock block, BOM table
  - **Still shows 2S3P/37.5F/24.8s/5W/6-cell throughout — ALL must be updated to 2S4P/50F/33.5s/15W/8-cell**
  - BOM Notes lock block (near line 531+) also needs 2S4P update
  - BOM table row `C_SC1–6` needs renaming to `C_SC1–8`
- `design/Electronics/Power_Module/Board_Layout.md`
  - ASCII supercap block still shows 2×3 (6 cells); needs 2×4 (8 cells) row added
  - Power chain line still shows 37.5F; needs 50F
  - Shadow zone 41×61mm needs updating to 41×81mm
- `design/Electronics/Extension/Design_Spec.md`
  - §5 Thermal root cause fixed (U1 active IC note + NEVER REMOVE warning)
  - No further changes needed
- `design/Electronics/Consolidated_BOM.md`
  - C_SC row shows 6 cells (Qty=6); needs updating to 8 cells
- `design/Guides/User_Manual.md`
  - §3.6: shows 37.5F/24.8s/6 cells — needs 50F/33.5s/8 cells; "3 min" charge → "9 min"
- `design/Software/Linux_OS/Power_Management.md`
  - Timeline table: ≥24.8s (×2) → ≥33.5s
- `design/Electronics/Boards_Overview.md`
  - PM description: "37.5F (6×... 2S3P), ≥24.8s" → "50F (8×... 2S4P), ≥33.5s"
- `design/Standards/Certification_Evidence.md`
  - "≥24.8 seconds" → "≥33.5 seconds"
- `.copilot/plan.md`
  - Stale Values needs: 37.5F, 24.8s, 2S3P, 6-cell, C_SC1–6, 5W load, 3-min charge → stale
  - Correct values: 50F, 33.5s, 2S4P, 8-cell, C_SC1–8, 15W load, 9-min charge
- `.copilot/agent-prompts/r52-review-prompt.txt`
  - Same stale values update needed

</important_files>

<next_steps>

**Immediate — cascade 2S4P changes across all docs (all items below are NOT yet done):**

1. **`PM/Design_Spec.md`** (most changes):
   - FR-PM-02: ≥24.8s → ≥33.5s; C_SC1–6 → C_SC1–8
   - FR-PM-07: 24.8s → 33.5s
   - DR-PM-07: 6×/2S3P/37.5F/C_SC1–6 → 8×/2S4P/50F/C_SC1–8
   - DR-PM-09: ≥24.8s at 5W → ≥33.5s at 15W
   - §1 Supercap Block: 2×3/6 cells/37×57/41×61 → 2×4/8 cells/37×77/41×81
   - §2 Storage: 6×/2S3P/37.5F/123.8J/24.8s/5W → 8×/2S4P/50F/503J/33.5s/15W
   - §2 Supercap Manager: 6-cell/2S3P/37.5F → 8-cell/2S4P/50F
   - §3 Sequencing step 4: 6-cell/37.5F/~3 min/24.8s/5W → 8-cell/50F/~9 min/33.5s/15W
   - §3 Sequencing step 5: ≥24.8s → ≥33.5s
   - BOM Notes supercap lock block: 2S3P/6 cells/37.5F/24.8s → 2S4P/8 cells/50F/33.5s/15W
   - BOM table: C_SC1–6/2S3P/6× → C_SC1–8/2S4P/8×
2. **`PM/Board_Layout.md`**: ASCII 2×3 → 2×4; labels 37.5F/6 cells → 50F/8 cells; shadow zone 41×61→41×81; power chain 37.5F→50F
3. **`User_Manual.md`**: 6 cells/25F×6/37.5F/24.8s/3 min → 8 cells/25F×8/50F/33.5s/9 min
4. **`Power_Management.md`**: ≥24.8s → ≥33.5s (×2 in timeline table)
5. **`Boards_Overview.md`**: 37.5F/6×/2S3P/24.8s → 50F/8×/2S4P/33.5s
6. **`Certification_Evidence.md`**: ≥24.8 seconds → ≥33.5 seconds
7. **`Consolidated_BOM.md`**: C_SC Qty 6 → 8
8. **`plan.md`**: add 37.5F/24.8s/2S3P/6-cell/5W/C_SC1–6/3-min-charge to Stale Values; update correct values
9. **`r52-review-prompt.txt`**: same stale values update
10. **Run markdownlint** (fix then clean check), **commit all**, **create checkpoint 029**

</next_steps>
