# Checkpoint 090 — BOM Strip All Complete

**Status:** Complete — awaiting "Let's lock this in" before git commit
**Session:** BOM description-strip pass (multi-session)
**Follows:** 084-pass2-audit-complete.md

---

## What Was Accomplished This Session

### Phase 1 — FB1 Ferrite Bead Formalisation (session 085–086)

- Selected TE Connectivity `BMC-Q2AY0600M (2-2176748-1)` as FB1 on the Stator board
- Added to Stator `Design_Spec.md` BOM and `Consolidated_BOM.md` / `all_boards_bom.json`
- MPN listed as `BMC-Q2AY0600M (2-2176748-1)` per user instruction
  (DigiKey `1712-2-2176748-1CT-ND`, Mouser `279-BMC-Q2AY0600M`, JLCPCB global sourcing/consignment)
- Datasheet created: `design/Datasheets/Altera-MAX-II-Handbook-datasheet.md`
  (references the handbook markdown, not a PDF; covers EPM240/EPM570 family)

### Phase 2 — Rotor BOM Structural Rewrite (session 087–088)

- Rotor `Design_Spec.md` §5 BOM: merged Board A + Board B into a single contiguous component table
  with unique refdes for all components (U1, U2, U3/U4 for FDC ICs per variant, J1–J14, etc.)
- `Rotor_26_Char_Design.md` §8 and `Rotor_64_Char_Design.md` §8 appended with variant-specific BOM tables
- Consolidated BOM: Rotor rows restructured — `Rotor (N=26)` and `Rotor (N=64)` board identifiers introduced;
  4 new rows inserted for N=26-only components (C16, C17, C24–C27, L5–L8)
- All Rotor refdes now contiguous without Board A/B differentiation

### Phase 3 — BOM Component Description Strip (session 089–090)

Goal: strip all circuit-function description text from board spec `Component` columns and Consolidated BOM
`Description/Usage` column so entries read like invoice lines (`[Manufacturer]` only, with approved prefixes).

**Board spec files stripped (11 total):**

| File | Status |
|---|---|
| `design/Electronics/Power_Module/Design_Spec.md` | ✅ Stripped, lint-clean |
| `design/Electronics/Controller/Design_Spec.md` | ✅ Stripped, lint-clean |
| `design/Electronics/JTAG_Daughterboard/Design_Spec.md` | ✅ Stripped, lint-clean |
| `design/Electronics/Settings_Board/Design_Spec.md` | ✅ Stripped, lint-clean |
| `design/Electronics/Encoder/Design_Spec.md` | ✅ Stripped, lint-clean |
| `design/Electronics/Actuation_Module/Design_Spec.md` | ✅ Already clean |
| `design/Electronics/Stator/Design_Spec.md` | ✅ Already clean |
| `design/Electronics/Reflector/Design_Spec.md` | ✅ Stripped, lint-clean |
| `design/Electronics/Extension/Design_Spec.md` | ✅ Stripped, lint-clean |
| `design/Electronics/Rotor/Design_Spec.md` | ✅ Clean (prior session) |
| `design/Electronics/Rotor/Rotor_26_Char_Design.md` | ✅ Clean (prior session) |
| `design/Electronics/Rotor/Rotor_64_Char_Design.md` | ✅ Clean (prior session) |

**Consolidated BOM (`design/Electronics/Consolidated_BOM.md`):**
- 205 Description/Usage cells replaced with `[Manufacturer]` annotations (plus all approved preserve prefixes)
- 4 new `Rotor (N=26)` rows inserted (C16, C17, C24–C27, L5–L8)
- 6 Board column updates (`Rotor` → `Rotor (N=26)` or `Rotor (N=64)` for variant-specific rows)
- 6 RefDes trims on Rotor rows
- Section 2 header: `ROT-A` → `ROT-26`, `ROT-B` → `ROT-64`
- 5 quantity corrections in Section 2 for ROT-64 (was carrying Board B count, now full N=64 build count)
- Lint-clean ✅

**JSON (`design/Electronics/all_boards_bom.json`):**
- 201 `description` field values stripped to `[Manufacturer]` (with approved preserve prefixes)
- All `"Rotor (Board A)"` → `"Rotor (N=26)"` (17 entries)
- All `"Rotor (Board B)"` → `"Rotor (N=64)"` (12 entries)
- JSON valid (round-trip parse confirmed) ✅

---

## Approved Preserve Prefixes Applied

| RefDes | Preserved text |
|---|---|
| PM C14,C15 | `see DEC-030 [Samsung]` |
| PM R12, R23 | `no JLCPCB stock [Bourns]` |
| PM U1 | `variant-locked do not change [Texas Instruments]` |
| JDB C10,C11 | `C0G/NP0 exception approved — only C0G in system [Kemet]` |
| JDB R2 | `see DEC-016 [Panasonic]` |
| JDB R6,R7,R8 | `see DEC-024 [Panasonic]` |
| JDB Y1 | `see DEC-022 [CTS]` |
| SBD C4 | `different qualified JLCPCB source C960916 [Samsung]` |
| SBD R66–R77 | `JLCPCB MOQ 40 [KOA Speer]` |
| SBD R81–R98 | `no JLCPCB stock [Panasonic]` |
| ENC J1 | `eBay sourcing only [generic]` |
| ENC SW1–SW40 | `eBay sourcing only [generic]` |
| AM J3–J6 | `manually-fit [Adam Tech]` |
| AM U1 | `JLCPCB consignment only [STMicroelectronics]` |
| STA R1 | `no JLCPCB stock [Bourns]` |
| ROT U2 | `JLCPCB MOQ 2 [Texas Instruments]` |
| ROT (N=26) U3 | `JLCPCB MOQ 2 [Texas Instruments]` |
| ROT (N=64) U4 | `JLCPCB MOQ 2 [Texas Instruments]` |

---

## Files Changed (uncommitted)

- `design/Electronics/Consolidated_BOM.md`
- `design/Electronics/all_boards_bom.json`
- `design/Electronics/Power_Module/Design_Spec.md`
- `design/Electronics/Controller/Design_Spec.md`
- `design/Electronics/JTAG_Daughterboard/Design_Spec.md`
- `design/Electronics/Settings_Board/Design_Spec.md`
- `design/Electronics/Encoder/Design_Spec.md`
- `design/Electronics/Reflector/Design_Spec.md`
- `design/Electronics/Extension/Design_Spec.md`
- `design/Electronics/Rotor/Design_Spec.md`
- `design/Electronics/Rotor/Rotor_26_Char_Design.md`
- `design/Electronics/Rotor/Rotor_64_Char_Design.md`
- `design/Datasheets/Altera-MAX-II-Handbook-datasheet.md`
- `design/Electronics/Stator/Design_Spec.md` (FB1 addition from session 085)

---

## Next Steps

1. Await "Let's lock this in" → commit all staged changes
2. After commit: decide on next workstream (Pass 3 review, KiCAD library prep, Settings Board rename, etc.)

---

## Standing Rules (from agent-directives.md)

- **NEVER** modify MPN/supplier PNs without explicit user confirmation
- **NEVER** commit without "Let's lock this in"
- **NEVER** bump version metadata unless user explicitly requests it
- Banned manufacturers: **Murata** (blanket ban); **TDK** (no new selections)
- Data lookup order: markdown datasheet → local PDF → online
- Cross-reference link style: bold backtick path `` **`design/path/file.md`** ``
