# Enigma-NG Project Todo List

> **Canonical deferred-work and open-action reference.** Updated as work progresses.
> See also `.copilot/plan.md` for current workstream status and `.copilot/agent-directives.md` for operational rules.
>
> **Design Log Open Questions** are tracked separately in `design/Design_Log.md` under `## Open Questions`.
> Do not duplicate them here — that file is the authoritative source for formally raised design questions.

Last updated: 2026-05-02

---

## Open Workstreams (Plan-Level)

Long-running workstreams; tracked in `.copilot/plan.md` Current Open Workstreams table.

| ID | Description | Source |
| --- | --- | --- |
| `extension-mechanical-usage` | Detailed switch/linkage geometry for Extension boundary carry is still needed; architectural answer (shared AM) is locked but physical linkage spec is not | `plan.md` |
| `coupon-testing-review` | Add and review board-level coupons and PAS-oriented test coverage so production boards do not retain test-only hardware | `plan.md` |
| `battery-connector-final-review` | Re-confirm Glenair `807-216-00ZNU6-6DY` contact assignment, `BATT_PRES_N` position, reserved-contact behaviour, cable selection, and interposer fit; check ODU AMC NP lead before closing | `plan.md` |
| `general-pin-mapping-schematic-capture` | Lock exact package pin/pad assignments for AM STM32, Stator mux U7, Encoder / Stator / Rotor CPLD packages — treat as one combined workstream aligned with KiCAD project and shared component library | `plan.md` |
| `rerun-deep-reviews` | Final pre-V1 cross-discipline deep-review cycle — run only once electrical, mechanical, and software work are complete and each board has a full KiCAD project with exported production Gerbers | `plan.md` |

---

## Electronics Deferrals

| ID | Description | Ref | Source |
| --- | --- | --- | --- |
| `ctlh1-deferred` | Controller CTL-H1 finding: explicitly deferred by user during Pass 2 review cycle | — | `handoff.md` note; Pass 2 deep-review |
| `rotor-esd-tvs` | Rotor ESD TVS (PRTR5V0U10AZ): Section 6 placeholder retained; final sourcing pending | — | `design/Electronics/Rotor/Design_Spec.md §6` |
| `rotor-variant-refdes-schematic` | Rotor N=26 vs N=64 variant U3/U4 placement in KiCAD: U3 and U4 are the same part in different board positions depending on variant; investigate KiCAD board variant / DNF flag approach so bypass caps (C6–C11) follow same variant logic | — | This session (2026-05-01); deferred until schematic capture |
| `display-addon-board` | Display add-on board design: J9 (Amphenol F52Q) on Controller is the only fixed connector; display power, touch wiring, and auxiliary harness remain deferred with the add-on board definition | DEC-033 | `design/Electronics/Controller/Design_Spec.md §8` |
| `cpld-production-replacement` | Review replacement CPLD for production stage (current MAX II EPM570 is a prototype-grade selection); update Certification Evidence §7.1 when confirmed | OA-04 | `design/Standards/Certification_Evidence.md` |
| `connector-thermal-verification` | Thermal / current-capacity verification of active PM and Stator dock connectors (TE `1-1674231-1` / `1123684-7` and Molex `2195630015` / `2195620015`); document final derating rule for Certification Evidence §5 | OA-05 | `design/Standards/Certification_Evidence.md` |
| `full-pn-review` | Full supplier PN review of all BOM entries before schematic capture — a prior session that reduced component package sizes appears to have corrupted supplier PNs on at least two components (ERJ-2RKF1001X, CL05B104KB5NNNC), substituting codes pointing to entirely different parts. A sweep of all DigiKey / Mouser / JLCPCB PNs against their MPNs is required before KiCAD work begins | — | 2026-05-02 supplier PN audit |
| `footprint-requests-pending` | Footprints requested but not yet received; update BOM and library when each arrives: **BAT54** (Diotec SOT-23) — requested, **AC72ABD** (72°C SMD thermal cutoff) — requested, **BMC-Q2AY0600M** (TE 600Ω 0805 AEC-Q200 ferrite bead) — requested. Add further pending requests here as they arise | — | 2026-05-02 |

---

## Mechanical Deferrals

| ID | Description | Source |
| --- | --- | --- |
| `rotor-shaft-diameter` | Central shaft hole diameter for Rotor PCBs: Ø10mm nominal; final size TBD once Rotor Actuation Assembly shaft diameter is fixed (8–12mm range) | `design/Mechanical/Rotor/Design_Spec.md`; `design/Electronics/Rotor/Board_Layout.md` |
| `rotor-rolling-element` | Rolling element diameter: TBD; matched set required for even load (±0.01mm) | `design/Mechanical/Rotor/Design_Spec.md` |
| `rotor-alloy-grade` | Rotor disc aluminium alloy grade: TBD — 6061-T6 suggested for machinability; confirm before manufacture | `design/Mechanical/Rotor/Design_Spec.md` |
| `rotor-shaft-mechanism` | Rotor shaft retention mechanism: TBD — pending Rotor Actuation Assembly spec | `design/Mechanical/Rotor/Design_Spec.md` |
| `display-aperture` | Main enclosure display aperture dimensions: TBD pending display size selection (up to 10" supported via DSI1); deferred display auxiliary hinge space also unresolved | `design/Mechanical/Main_Enclosure/Design_Spec.md` |
| `system-assembly-harnesses` | Complete System Assembly cable harness definitions: TBD — 20-pin encoder IDC ribbons, reflector cable, fan cable, User Settings Module I²C ribbon, switch / battery harnesses | `design/Mechanical/Complete_System_Assembly/Design_Spec.md` |
| `system-assembly-connectors` | Complete System Assembly connector list: TBD — TE PM dock, Molex Stator dock, ERF8/ERM8 rotor-family BtB, JST PH servo, JST SH fan, 20-pin IDC encoder, etc. | `design/Mechanical/Complete_System_Assembly/Design_Spec.md` |

---

## Software Deferrals

| ID | Description | Ref | Source |
| --- | --- | --- | --- |
| `ltc3350-telemetry` | LTC3350 I²C telemetry support in Linux OS power-management driver: deferred to Software PoC stage, pending hardware availability | DEC-025 | `design/Software/Linux_OS/Power_Management.md §2` |
| `cpld-timing-load` | CPLD Encoder Logic timing and electrical load characterisation (propagation delays, fanout, drive current): deferred until first prototype boards exist for measurement | — | `design/Software/CPLD_Logic/Encoder_Logic.md §2` |

---

## Standards & Certification Actions

Items from `design/Standards/Certification_Evidence.md §8`.

| ID | Description | Priority | Status |
| --- | --- | --- | --- |
| DA-01 | If coupon-based diagnostic access is introduced, exposed ENIG pads require dedicated ESD protection or documented justification before production release and classroom deployment | Post-coupon design | Open |
| DA-02 | ESD policy for classroom deployment variant: define which internal BtB-accessible connections require additional ESD protection in educational / student-access configuration | Pre-production | Open |
| DA-03 | Full consistency documentation pass: legacy Link-Alpha / Link-Beta references must remain historical-only after DEC-038; verify any new docs added use TE PM dock / Molex Stator dock naming | Ongoing | Open |
| DA-04 | Update Consolidated BOM with all locked Power Module components *(may be superseded by the 2026-05 BOM restructure — verify against current `Consolidated_BOM.md` before actioning)* | Post-eFuse lock | Review needed |
