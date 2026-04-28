# Checkpoint 074 — Datasheet Hygiene Complete

## Summary

Completed full datasheet coverage audit and hygiene pass for all BOM components.

## Changes Made

### BOM §11 Datasheet Links — Samtec fixed
- Lines 544–545: corrected broken link `samtec-erm8-erf8-datasheet.md` (did not exist)
  to individual files: `erf8-xxx-xx.x-xxx-dv-xxxx-xx-mkt-datasheet.md` and
  `erm8-xxx-xx.x-xxx-dv-xxxx-xx-mkt-datasheet.md` (both files confirmed present)

### BOM §11 Datasheet Links — 5 new entries added
- Samsung CL21B106KAYQNNE (10µF 25V X7R 0805 bulk cap, 212 units) → `Samsung-1276_CL21B1-datasheet.md`
- Kyocera AVX KAM05CR71A105KH (1µF 10V X7R 0402 FDC dec cap) → `KAM05CR71A105KH-Datasheet.md`
- Yageo CC1206KKX7R8BB106 (10µF 16V X7R 1206 MIC1555 timing cap) → `Yaego-UPY-GPHC_X7R_6_3V-TO-250V-CC1206KKX7R8BB106-datasheet.md`
- TDK CGA9N3X7R1E476M230KB (47µF 25V X7R 2220 buck output cap) → `TDK-CGA_mlcc_automotive-datasheet.md`
- TDK CGA6P3X7R1H475K250AD (4.7µF 50V X7R 1210 entry filter cap) → `TDK-CGA_automotive-datasheet.md`

### Inventory JSON updated
- Added 7 new `pdf_to_markdown` entries: ERM8, ERF8, Samsung, KAM05, Yageo, TDK×2

### Orphaned datasheets removed
- `Kyocera-AVX-KGP-datasheet.md` — KGP Stack Capacitor series; confirmed zero references in
  any design or BOM file. Not a BOM component. Deleted.
- `Kyocera-AVX-KGP-datasheet.pdf` — matching PDF also deleted.

### Git housekeeping
- `.copilot/checkpoints/057-size-down-pass-complete.md` — deleted from disk in prior session
  but never staged. Staged and removed from index in this session.

## Audit Results

| Check | Result |
|:---|:---|
| Samtec ERM8/ERF8 broken link | ✅ Fixed — pointed to correct individual files |
| Samsung CL21B106KAYQNNE in §11 | ✅ Added |
| KAM05CR71A105KH in §11 | ✅ Added |
| CC1206KKX7R8BB106 in §11 | ✅ Added |
| TDK CGA caps in §11 | ✅ Added (2 entries) |
| KGP orphan confirmed and removed | ✅ Done |
| No `.pdf` direct links in design specs | ✅ Confirmed clean |
| Old CL31B106KBHNNNE fully removed | ✅ Confirmed (prior session) |
| CC1206KKX7R8BB106 still active (PM C42) | ✅ Confirmed not redundant |

## Open Work After This Checkpoint

- Controller Board open items (from deep-review cycle):
  - LED resistor BOM consolidation (use existing 0402 Panasonic ERJ parts)
  - PWR_BUT → dedicated CM5 power button pin (recurring — must be pinned)
  - VDD_GPIO_REF decoupling cap definition
  - DSI display power per CM5 datasheet
- Category C battery connector sourcing (pending supplier email responses)
- Extension/Reflector/AM/JDB review cycle findings (agents were running but results need actioning)
