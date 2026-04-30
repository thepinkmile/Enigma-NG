# Checkpoint 079 — DEC-048: ESD protection extended to host-side BtB connectors

## Status

All work committed and clean. Commit: `e4fc252`

## What was done

### Context

All six prior deep-review items were confirmed resolved at the start of this session.
One stale prose sentence in `Rotor/Design_Spec.md` was corrected.

The user raised an ESD/TVS gap: DEC-045 protected only the Rotor board side of
each Samtec ERM8/ERF8 BtB connector. During live rotor swap, both faces are
simultaneously exposed to operator handling. DEC-048 was defined and implemented
to extend the same TPD4E05U06QDQARQ1 ESD arrays to all host-side rotor-facing
connectors (Stator, Extension, Reflector).

### Files modified

| File | Change |
| :--- | :--- |
| `design/Electronics/Rotor/Design_Spec.md` | Stale "still-deferred" prose at §2.1 replaced with cross-reference |
| `design/Electronics/Stator/Design_Spec.md` | FR-STA-13, DR-STA-16 added; §8 ESD rewritten; BOM U9–U12 added |
| `design/Electronics/Extension/Design_Spec.md` | FR-EXT-07, DR-EXT-13 added; §5 ESD rewritten; BOM U2–U9 added |
| `design/Electronics/Reflector/Design_Spec.md` | FR-REF-05, DR-REF-06 added; §5 renamed to "Thermal & ESD" and populated; BOM U1–U4 added |
| `design/Design_Log.md` | DEC-048 entry added |
| `design/Electronics/Consolidated_BOM.md` | Section 1: STA/EXT/REF rows added; Section 2 row 13 updated (total 28 arrays) |
| `.copilot/review-report.md` | Pass 18 closing entry added — all items confirmed resolved |
| `.copilot/agent-directives.md` | Primary directive language touch-up |

### DEC-048 scope

**Protected (TVS required):** All Samtec ERM8/ERF8 connector faces exposed during live rotor swap.

| Board | Connectors | Arrays | RefDes |
| :--- | :--- | :--- | :--- |
| Stator | J1 (JTAG ERF8-005), J3 (ENC ERF8-010) | 4× TPD4E05U06QDQARQ1 | U9–U12 |
| Extension | J1/J4 (JTAG), J3/J6 (ENC) — both sides | 8× TPD4E05U06QDQARQ1 | U2–U9 |
| Reflector | J1 (JTAG ERM8-005), J3 (ENC ERM8-010) | 4× TPD4E05U06QDQARQ1 | U1–U4 |

**Explicitly excluded:** power-only BtB pairs, Stator J4–J13 (IDC/ribbons/docks/harness),
Extension J7/J8 (BHR-20-VUA ribbons), Extension J9/J10 (AM service docks), Reflector J4
(TTD_RETURN ribbon).

### TVS device

TPD4E05U06QDQARQ1 — 4-channel bidirectional ESD array, USON-10, passive (no VCC pin, no bypass cap).

- Mouser: 595-PD4E05U06QDQARQ1 *(user-confirmed correct, NOT a typo)*
- DigiKey: 296-40696-1-ND
- JLCPCB: C81353

### Review status

Pass 18 added to `review-report.md` — all deep-review cycle items confirmed closed.
No new unsourced parts introduced.

## Next steps

- KiCAD shared library work (footprint verification and import)
- Schematic capture can begin once library is ready
