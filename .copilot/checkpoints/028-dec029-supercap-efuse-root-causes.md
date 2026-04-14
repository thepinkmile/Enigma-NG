# Checkpoint 028 — DEC-029 supercap hold-up spec; eFuse & Extension U1 root causes fixed

**Date:** 2026-04-14
**Commit:** acae80d (and prior: c8b0bd4, cb0901c, f188851)
**Session:** bb01fc15

---

## What Was Done

### Root cause analysis and permanent fixes for three recurring regressions

Three bugs that had survived multiple review cycles were traced to root causes in the design
documentation itself and fixed at source.

---

### 1. eFuse MPN regression (TPS259804ONRGER ↔ TPS259807)

**Root cause:** Stored session memories contained TPS259807 as the "correct" part. The live
design docs were already correct (TPS259804ONRGER throughout), but the conflicting memory
caused future review agents to revert to TPS259807.

**Fixes applied:**
- `PM/Design_Spec.md` BOM Notes: `⚠️ eFuse variant lock` block added showing 04=correct,
  07/03=wrong, with OVLO rationale. Any proposed MPN change requires explicit justification.
- `Design_Log.md` DEC-005: expanded with identical variant lock table.
- Session memories updated: TPS259804ONRGER confirmed correct (16.9V silicon-fixed OVLO,
  cut-tape, ONRGER = orderable MPN on Mouser/DigiKey).
- `plan.md` Critical Notes: Part Number Change Rule added — datasheet must exist in
  `design/Datasheets/` before any MPN change may be applied.
- `r52-review-prompt.txt`: Part Number Change Rule added as instruction #8.

---

### 2. Extension U1 buffer removal (SN74LVC2G125DCUR kept being flagged/removed)

**Root cause:** `Extension/Design_Spec.md` §5 Thermal contained the phrase
`"Passive components only."` — this caused review agents to conclude the Extension board had
no active components and flag U1 as anomalous, leading to its removal in review fixes.

**Fix applied:**
- `Extension/Design_Spec.md` §5: replaced "Passive components only." with explicit statement
  that U1 is the only active IC (<10mW), no heatsinking required, C6 is its bypass cap, and
  a `⚠️ U1 must never be removed` warning with references to FR-EXT-01/02, DR-EXT-04/05/06.
- `plan.md` Stale Values: added `"Passive components only" for Extension §5` as a prohibited phrase.
- `r52-review-prompt.txt` Stale Values: added same prohibition.

---

### 3. Supercap stale values (22F / 33F / 21.7 s)

**Root cause:** When checkpoint 025 upgraded PM Design_Spec to Abracon 25F cells, six other
files were not updated and continued to show the pre-Abracon 22F/33F/21.7s values. Review
agents found the majority of docs saying 22F/33F and reverted PM Design_Spec to match.

**Stale value sweep (all → corrected values):**

| File | Was | Now |
|:---|:---|:---|
| `PM/Board_Layout.md` (ASCII diagram, power chain) | 22F×6 cells, 33F/5.4V | 25F×6 cells, 37.5F/5.4V |
| `User_Manual.md` §3.6 | 22F each, 33F at 5.4V, ≥21.7s | 25F each, 37.5F at 5.4V, ≥24.8s |
| `Power_Management.md` timeline table | ≥21.7s (×2) | ≥24.8s (×2) |
| `Boards_Overview.md` §9 | 33F, ≥21.7s | 37.5F (6× Abracon 25F/2.7V, 2S3P), ≥24.8s |
| `Certification_Evidence.md` §3.5 | ≥21.7 seconds | ≥24.8 seconds |
| `Design_Log.md` DEC-004 rationale | 6× 22F supercap bank | 6× 25F supercap bank (Abracon ADCR-T02R7SA256MB) |

**Lock notes added:**
- `PM/Design_Spec.md` BOM Notes: `⚠️ Supercap cell lock` block with full parameter table
  (25F/2.7V, 2S3P, 37.5F, 123.8J, ≥24.8s) and explicit prohibition on 22F/33F/21.7s.
- `Design_Log.md` DEC-021: post-decision update note recording the Abracon upgrade.
- `plan.md` and `r52-review-prompt.txt`: 22F/33F/21.7s added to Stale Values list.

---

### 4. DEC-029 — New authoritative supercap hold-up specification

**Added to `Design_Log.md`:**

- **DEC-004** status changed: `Decided` → `Superseded by DEC-029`
  (0.5A charge current constraint retained in DEC-029; only cell reference was stale)
- **DEC-021** status changed: `Accepted` → `Superseded by DEC-029`
  (2S3P arrangement retained; cell capacitance 22F → 25F Abracon documented in DEC-029)
- **DEC-029 created** (new, Accepted 2026-04-14):
  - Confirmed cell: Abracon ADCR-T02R7SA256MB, 25F/2.7V, 2S3P, 6 cells, 37.5F at 5.4V
  - ≥20s hold-up requirement stated explicitly with cell lock warning
  - Full hold-up calculations included:
    - Conservative (pure-buck, V_lo=4.75V): 123.7J → **≥24.7s** ✅
    - Realistic (LTC3350 boost, V_lo=2.0V, η=85%): 401J → **≈80s** ✅
    - Minimum to hit 20s: V_lo only needs to reach 4.88V (trivially achievable)
  - 0.5A PoE charge current from DEC-004 retained and explained
  - LTC3350 CELLS register = 0x01 (2 series cells) documented

---

## Files Modified

- `design/Design_Log.md` — DEC-004/021 superseded; DEC-029 added; DEC-021 post-note added; DEC-004 cell ref updated
- `design/Electronics/Extension/Design_Spec.md` — §5 "Passive components only" root cause fixed
- `design/Electronics/Power_Module/Design_Spec.md` — Supercap cell lock block added to BOM Notes
- `design/Electronics/Power_Module/Board_Layout.md` — 22F/33F → 25F/37.5F (ASCII + power chain)
- `design/Electronics/Boards_Overview.md` — 33F/21.7s → 37.5F/24.8s
- `design/Guides/User_Manual.md` — 22F/33F/21.7s → 25F/37.5F/24.8s
- `design/Software/Linux_OS/Power_Management.md` — ≥21.7s → ≥24.8s (×2)
- `design/Standards/Certification_Evidence.md` — ≥21.7s → ≥24.8s
- `.copilot/plan.md` — Stale Values list updated; Part Number Change Rule added
- `.copilot/agent-prompts/r52-review-prompt.txt` — Stale Values updated; Part Number Change Rule added

## State

markdownlint: **CLEAN** (0 warnings)
Committed: `acae80d`
