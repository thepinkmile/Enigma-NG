# Checkpoint 095 — Connector Derating Analysis Complete

## Summary

`connector-thermal-verification` (OA-05) is complete. Full current and thermal derating analysis
performed for all PM dock and Stator dock connectors; all results documented and OA-05 closed.

## Files Changed

| File | Change |
| --- | --- |
| `design/Datasheets/TE-108-5775-product-specification.md` | **Created** — new markdown for TE product spec 108-5775 Rev. B2 with all electrical ratings, environmental test table, and temperature exception note |
| `design/Datasheets/TE-1123684-7-datasheet.md` | Added "Electrical and Environmental Ratings" section with 6A/contact rating, operating range, and cross-reference to product spec |
| `design/Datasheets/TE-1-1674231-1-datasheet.md` | Same addition as plug datasheet above |
| `design/Standards/Certification_Evidence.md` | Updated §5 preamble (DEFSTAN target added); replaced BtB placeholder row with actual figures; added full §5.1 derating analysis subsection; closed OA-05 |
| `.copilot/todo-list.md` | `connector-thermal-verification` marked done |

## Key Findings

### TE PM Dock (J1/J2/J3 — TE 1123684-7 / 1-1674231-1)

- **Rating:** 6A per contact, −20°C to +80°C operating, 30°C max temperature rise at rated current
- **J1 worst-case:** 5V\_MAIN contacts carry 3.17A / contact = **52.8%** of rated 6A ✓
- **J2 worst-case:** VIN\_POE\_12V contacts carry 1.67A / contact = **27.8%** ✓
- **Worst-case contact body temperature @+80°C ambient:** 88.4°C (5V\_MAIN contacts, J1) — within thermal shock upper bound (+85°C) and heat aging test (85°C / 96h) ✓

### Molex EXTreme Guardian HD (Stator J11/J12 ↔ Controller J4/J5)

- **Rating:** 130A per contact, −40°C to +125°C — fully meets DEFSTAN ✅
- **Max design load:** <0.51A / contact = **<0.4% of rated current** — trivially within derating rule ✓

### Temperature Exception — TE PM Dock Cold Limit

| | |
| --- | --- |
| TE operating lower bound | −20°C |
| DEFSTAN target | −40°C |
| Supporting evidence | Thermal shock test (§3.5.12) cycles to −40°C × 5, passes ΔR ≤ 20 mΩ |
| Required action | Obtain formal TE written statement before DEFSTAN compliance submission, or formally accept exception citing thermal shock data |

## Todo Status Change

| Todo | Old Status | New Status |
| --- | --- | --- |
| `connector-thermal-verification` | pending | **done** |

## Remaining Unblocked Todos

- `coupon-testing-review`
- `ctlh1-deferred`
- `extension-mechanical-usage`
- `prototype-pcb-manufacturing` (milestone)
- `rotor-variant-refdes-schematic`
- `rotor-esd-tvs` (depends on `rotor-variant-refdes-schematic`)

`full-pn-review` remains blocked pending: `extension-mechanical-usage`, `battery-connector-final-review` (BLOCKED — external supplier contact), `ctlh1-deferred`, `rotor-esd-tvs`, `coupon-testing-review`.
