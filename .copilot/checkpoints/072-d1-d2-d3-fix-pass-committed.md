# Checkpoint 072 — D1/D2/D3 fix pass committed

## Status
All deep-review fix passes (F1–F6 and D1–D3) are committed and the working tree is clean.

## What was done this checkpoint
- Fixed all remaining markdownlint errors from D1/D2/D3 edits:
  - MD013 (line-length) in Global_Routing_Spec.md §9 bullets (x3), Extension §5 ESD text, Stator §8 ESD text
  - MD060 (pipe-space) in Consolidated_BOM.md line 61, Extension Design_Spec lines 176+186, Stator Design_Spec line 383
- Confirmed lint clean across all 6 changed files
- Committed: da3df20 — "Electronics deep-review fix pass: Extension/AM/JDB/Stator + D1/D2/D3 decisions"

## Files changed (this commit)
- `design/Electronics/Actuation_Module/Design_Spec.md` — DR-AM-08 100nF→1µF, C1 BOM 0402→0805 (D3)
- `design/Electronics/Consolidated_BOM.md` — UNSOURCED ESD rows removed; AM §4c C1 updated; matrix pipe-space fixed
- `design/Electronics/Extension/Design_Spec.md` — R1 removed (D1); ESD text replaced (D2); pipe-space fixes
- `design/Electronics/JTAG_Daughterboard/Design_Spec.md` — F5/F6 fixes: FT232HL LQFP-48, C6-C9 decoupling, R3 pull-up
- `design/Electronics/Stator/Design_Spec.md` — ESD text replaced (D2); D1 BOM row removed; pipe-space fix
- `design/Standards/Global_Routing_Spec.md` — §9 ESD/TVS rule added (external only); line-length fixes

## Decisions applied
- **D1:** Extension R1 GND isolating resistor removed — system GND is shared, no isolation needed
- **D2:** ESD/TVS only on external-facing connectors; all internal connectors exempt; rule codified in Global_Routing_Spec.md §9
- **D3:** AM C1 debounce cap 100nF → 1µF (10ms RC); reuses Kemet C0805C105K5RACTU already in BOM

## SQL state
- `review-extension-reflector-am-jdb` → done

## Remaining work
- Size-down pass: bulk caps 1206→0805 where voltage margins permit; 0603→0402 consolidation
- Controller Board open items (LED resistor BOM consolidation, PWR_BUT CM5 pin, VDD_GPIO_REF decoupling cap, DSI display power)
- Category C battery connector sourcing (awaiting supplier emails)
- New-component sourcing todo list (size-down candidates and CRIT items from power module review)
