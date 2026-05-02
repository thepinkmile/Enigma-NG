# Checkpoint 101 — BOM encoding, merge review, and C20 correction complete

**Date:** 2026-05-08 (evening/night session)
**Preceding checkpoint:** 100 (datasheet design-content cleanup)

---

## What was accomplished

### 1. Five BOM fix categories applied to `design/Electronics/Consolidated_BOM.md`

Applied all five approved fix categories via Python fix script:

- **Encoding fix**: 1,349+ mojibake substitutions (CP1252-as-UTF-8):
  `ÔÇö→—`, `┬ÁF→µF`, `╬®→Ω`, `┬▒→±`, `┬▓→²`, `├ù→×`, `Ô£ô→✔`, `ÔëÇ→≈`, `┬░→°`, `├╝→ü`
  Also fixed two missed instances not in original map: `┬ÁH→µH` (lines 50 and 147 —
  SRP1265A-100M and CWF1610A-180K inductors).
- **Mouser PN fix**: `595-TPD4E05U06QDQARQ1` → `595-PD4E05U06QDQARQ1`
  (Mouser convention: leading T dropped).
- **PM C20 Kemet 1206 row deleted**: removed incorrect standalone row
  (DigiKey `399-C1206C106K3RACTUCT-ND`, Mouser `80-C1206C106K3R`, JLCPCB `C2168111`).
- **PM C20 merged into Samsung CL21B106KAYQNNE row**: prepended `PM: C20;` to Board column;
  PM Qty `—`→`1`; System Qty `61`→`62`.
- **4 rotor-common row RefDes and qty corrections**:
  - RS1-05-G: added J9 to ROT-26; Sys 4→7
  - PH1-05-UA: added J13 to ROT-26; Sys 8→11
  - 219-6LPSTR: added SW3 to both variants; Sys 3→6
  - RS1-07-G: added ROT-26 instance; ROT-26 qty `—`→`1`; Sys 1→2
- **Section 2 deleted**: removed MPN Quantity Summary block (derived/redundant);
  archived in `.recycle-bin/consolidated_bom_original.md`.
- BOM reduced: 277 → 151 lines ✔

### 2. Encoder BT1–BT64 → J3–J66 BOM fix

Discovered that after the BOM was rebuilt from board specs (sessions after checkpoint 099),
the Encoder row reverted to the old `BT1–BT64` RefDes. Fixed to match the Encoder Design Spec
and Board Layout (both correctly show `J3-J66` since checkpoint 099).

| File | Fix |
| --- | --- |
| `design/Electronics/Consolidated_BOM.md` | `ENC: BT1-BT64` → `ENC: J3-J66` |

### 3. Power Module Design_Spec.md — C20 corrected to Samsung 0805

Three locations updated in `design/Electronics/Power_Module/Design_Spec.md`:
- Narrative component list (~line 211): `10µF 25V X7R 1206 (Kemet)` → `10µF 25V X7R 0805 (Samsung CL21B106KAYQNNE)`
- BOM table (~line 468): Manufacturer Kemet→Samsung, Spec 1206→0805, all three supplier PNs
  updated: DigiKey `1276-CL21B106KAYQNNECT-ND`, Mouser `187-CL21B106KAYQNNE`, JLCPCB `C3039694`
- Design rationale (~line 617): C20 description updated to match Samsung part

### 4. Stray temp files deleted from repo root

- `bom_section1_new.txt` — deleted ✔
- `build_bom_section1.py` — deleted ✔

### 5. MPN merge analysis — no merges required

Scanned all data rows in the current BOM (151 lines). All same-MPN multi-board parts are already
on single rows. Only exception is `ERJ-2RKF1001X` (1kΩ 1% 0402) which is intentionally split
across two rows (PM vs SBD) due to different JLCPCB stock codes (C25705 vs C242161) — this is
documented in BOM Notes at line 21 and must **not** be merged.

---

## Files changed this session

| File | Change |
| --- | --- |
| `design/Electronics/Consolidated_BOM.md` | Encoding fix, Mouser PN fix, PM C20 merge, Section 2 deleted, 4 rotor row fixes, BT1–BT64→J3–J66 |
| `design/Electronics/Power_Module/Design_Spec.md` | C20 corrected to Samsung CL21B106KAYQNNE 0805 (3 locations) |
| `bom_section1_new.txt` (repo root) | Deleted |
| `build_bom_section1.py` (repo root) | Deleted |

Both surviving files passed `markdownlint` with exit code 0 ✔

---

## Key technical notes

- **ERJ-2RKF1001X intentional split**: PM row uses JLCPCB C25705, SBD row uses C242161 — different
  stock codes. DigiKey PNs also differ. Documented at BOM Notes line 21. Never merge.
- **PM C20 history**: Old BOM had both a Kemet 1206 row (incorrect) and a Samsung 0805 row (correct).
  Resolution: delete Kemet row, prepend `PM: C20;` to Samsung row. Design_Spec.md is authoritative —
  confirms Samsung 0805 per prior user approval.
- **Section 2 was derived/redundant**: deleted and archived in `.recycle-bin/`.
- **BOM column order (17 qty cols + metadata)**: Board (RefDes) | MPN | DigiKey PN | Mouser PN |
  JLCPCB PN | Alt Supplier+PN | PM | CTL | JDB | SBD | ENC | AM | STA | REF | EXT | ROT-26 | ROT-64
  | System Qty | Notes | Footprint Available | Footprint Downloaded

---

## Commit status

**NOT YET COMMITTED** — awaiting explicit "Let's lock this in" from user (morning review).

---

## Next session start point

1. `.copilot/agent-directives.md`
2. `.copilot/plan.md`
3. `.copilot/handoff.md`
4. `.copilot/todo-list.md`
5. This checkpoint
