# Cypher Board Grounding and Shielding Clarification

This discussion is a grounding/EMC clarification only. Connector family and
board-edge hardware details are superseded by
`.copilot/discussions/extension-mechanical-usage.md`; this file only carries
the `GND_CHASSIS` intent and enclosure assumptions needed to merge the
grounding rules later.

## 1. Board Naming and Scope

This note applies to the four-board chassis using the active board names:

- **Cypher**
- **Stack-Input**
- **Stack-Output**
- **Stack-Blanking**

The intent is to clarify chassis grounding and shielding without changing the
current extension discussion. The extension discussion remains authoritative for
stackup, connector selection, and signal mapping.

### 1.1 Stackup Authority

- The **Cypher board remains 6-layer**.
- The other boards retain the stackups already defined in the extension discussion.
- The earlier assumption that all boards were at least 4-layer is not authoritative for the Cypher board and must not be used to downgrade it.

## 2. Prototype Enclosure Assumptions

The following values are retained only as initial prototype estimates to support enclosure mockups:

- **Shell wall thickness:** 1.2 mm
- **Internal air gap:** 0.8 mm
- **Raw edge to mating face offset:** 2.0 mm

These values are not final enclosure dimensions. They are only the early mechanical estimates used to drive prototype case design while boards are still being validated.

## 3. `GND_CHASSIS` and Logic Ground

The chassis uses two distinct ground concepts:

- **`GND`**: the logic ground used on the boards and connector pinouts defined in the extension discussion
- **`GND_CHASSIS`**: the perimeter shield ring used for EMC/ESD containment

The intent is:

1. `GND_CHASSIS` must connect to `GND` at **one and only one point** on the Power Module.
2. No additional `GND_CHASSIS`-to-`GND` ties should be added on the other boards.
3. Board-edge ground pins remain part of the logic ground system, not a second chassis return path.

## 4. Shielding Rules Around the Board Edges

The `GND_CHASSIS` ring should be continuous around the chassis except where it must be relieved locally around the right-angle connector zones.

- The local break is only to maintain clearance around the connector openings.
- The break must not introduce any second connection between chassis ground and logic ground.
- The edge treatment should avoid turning the box sides into an antenna or creating grounding loops.

```text
             ◄──────────── 4.0mm Keep-Out ──────────────►
[BOARD EDGE] ──► [2.5mm GND_CHASSIS] ──► [1.5mm MOAT] ──► [INNER LOGIC ZONE]
```

For the Stack-Input and Stack-Output boards, the connectors are already right-angle in the current design. This discussion only captures the shielding cut-out and continuity intent around those connectors.

```text
       [GND_CHASSIS PLATED HOLE] ──► (Clamped to Metal Enclosure Frame)
                  │
 ┌────────────────┴────────┐              ┌────────────────────────┐
 │   PCB GND_CHASSIS Ring  │              │  PCB GND_CHASSIS Ring  │
 ├─────────────────────────┤  [OPEN GAP]  ├────────────────────────┤
 │     ISOLATION MOAT      │  (No Moat)   │     ISOLATION MOAT     │
 └─────────────────────────┘ ┌──────────┐ └────────────────────────┘
                             │  QSS-RA  │ ◄── Logic GND & Traces
                             └──────────┘     Extend Fully To Edge
```

## 5. Relationship to the Extension Discussion

This file extends Entry 20 from the extension discussion only for EMC/grounding clarity.

- It does **not** replace the extension discussion.
- It does **not** change the Cypher board stackup.
- It does **not** re-open connector selection.
- When merged later, only the `GND_CHASSIS` / shielding clarification should be pulled into the authoritative discussion.

## 6. Active Design Impact Review (Current Repository State)

The current active design already captures the core single-point grounding model:

- `design/Standards/Global_Routing_Spec.md §5` already enforces one global `GND` ↔ `GND_CHASSIS` bond on the Power Module only.
- `design/Standards/Certification_Evidence.md §2.2` already records the same EMC rationale.
- Existing board `Design_Spec.md` files for enclosure-connected boards already state "local `GND_CHASSIS`, no local bond."

Therefore, this discussion is mostly an extension/clarification, not a topology reversal.

### 6.1 Delta Needed vs Current Active Design

| Area | Current status | Required update |
| --- | --- | --- |
| Global single-point bond rule | Already defined and consistent | No topology change required |
| Chassis ring geometry | Not globally standardized across all board docs | Add a new `Global_Routing_Spec.md` rule defining default geometry (2.5 mm ring + 1.5 mm moat = 4.0 mm total edge keep-out), cross-reference it from all enclosure-connected board specs, explicitly state non-usage on module boards (JTAG Module, Actuation Module, CM5 context), and link the new rule to `Global_Routing_Spec.md §5` single-point `GND` ↔ `GND_CHASSIS` bond rule |
| Connector-window break rule | Not explicitly documented as a global rule | Add this as an explicit caveat under the new GRS chassis-ring geometry rule: where an external connector is located, a local `GND_CHASSIS` ring break/relief is required because the connector signal pins cannot be terminated inside the ring/moat keep-out zone |
| Anti-loop treatment | Single-point bond is defined; local ring-break method is not fully codified | Add explicit "no second bond, no loop closure via board copper" language at standards level |

## 7. Chassis-Connected Board Tracking (Non-Module Boards)

Scope requested: include boards that are part of chassis grounding continuity; exclude module boards carried by other boards (JTAG Module, Actuation Module, CM5).

### 7.1 Existing Active Boards

| Board | Current `GND_CHASSIS` status | Change needed from this discussion |
| --- | --- | --- |
| Power Module | Single-point bond host and chassis features already defined | Keep as sole bond point; align wording to ring/window global rules when added |
| Controller | Local chassis net and no local bond already defined | Reference the new GRS chassis-ring rule instead of duplicating ring geometry locally; only call out board-specific `GND_CHASSIS` ring breaks at external connector zones (e.g. HDMI, Ethernet, USB) and keep connector chassis bonds on `GND_CHASSIS` rather than signal `GND` where applicable |
| Encoder | Treated as active in legacy docs, but moving forward is considered a module | Mark as module-context going forward; no standalone `GND_CHASSIS` ring detail required |
| Extension | Active legacy board, but being retired by extension-mechanical-usage replacement boards | No further ring-detail propagation required in this track |
| Stator | Active legacy board, but being retired by extension-mechanical-usage replacement boards | No further ring-detail propagation required in this track |
| Reflector | Active legacy board, but being retired by extension-mechanical-usage replacement boards | No further ring-detail propagation required in this track |
| Rotor (A+B) | Dual-board assembly remains active and enclosure-coupled via metal rotor enclosure path to main chassis | Both rotor PCBs shall implement `GND_CHASSIS` perimeter ring per new GRS chassis-ring rule; no local `GND` ↔ `GND_CHASSIS` bond on rotor boards |
| User Settings Module | Local chassis net + no local bond already defined; remains relevant as remote extension board | Keep explicit reference to the new GRS chassis-ring rule |

### 7.2 Upcoming Replacement Boards from Extension Discussion

| New board | Status in active design files | Required chassis-ground work before implementation close |
| --- | --- | --- |
| Cypher | Not yet implemented as active board files | Add cross-reference to the new GRS chassis-ring rule; document only board-specific connector ring-break/gap caveats where required |
| Stack-Input | Not yet implemented as active board files | Add cross-reference to the new GRS chassis-ring rule; document only board-specific connector ring-break/gap caveats where required |
| Stack-Output | Not yet implemented as active board files | Add cross-reference to the new GRS chassis-ring rule; document only board-specific connector ring-break/gap caveats where required |
| Stack-Blanking | Not yet implemented as active board files | Add cross-reference to the new GRS chassis-ring rule; document only board-specific connector ring-break/gap caveats where required |
