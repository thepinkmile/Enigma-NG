# DEC-084 - Cypher-Stack Architecture Migration and Board-Role Consolidation

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-084|
|**Status**|Confirmed|
|**Date**|2026-07-04|
|**Author**|Izzyonstage & GitHub Copilot|
|**Supersedes**|Architectural ownership model of standalone Stator/Reflector/Extension/JTAG Module/Actuation Module in active topology|

## Context

The merged extension-mechanical architecture discussions define a new active board topology centered on
Cypher Board + mini-stack boards, with clear migration away from several legacy standalone board roles.
The design now requires one consolidated decision entry to anchor this migration in the main design set.

## Decision

Adopt the cypher-stack merged architecture as the active migration baseline:

1. **Cypher Board** becomes the central cipher backplane and replaces standalone Stator + Reflector
   ownership in the active architecture.
2. **Stack-Input** and **Stack-Output** replace standalone Extension ownership for
mini-stack ingress/egress.
3. **Stack-Blanking** is the passive end-of-chain routed termination board.
4. **Input-Cypher** and **Output-Cypher** are the active user-facing cypher-side boards.
5. Standalone **JTAG Module** and standalone **Actuation Module** ownership migrate into the new active
   board set (Cypher and Stack-Input respectively).

## Rationale

The merged topology is mechanically and electrically consistent with the current discussion outcomes,
reduces split ownership across legacy boundaries, and provides a clean architecture baseline for applying
the merged discussions into the main design before final component/BOM lock.

## Impact

1. Main architecture docs are updated to use the merged board set and migration ownership model.
2. New board-level design specs are created for:
   - Cypher_Board
   - Stack_Input_Board
   - Stack_Output_Board
   - Stack_Blanking_Board
   - Input_Cypher_Board
   - Output_Cypher_Board
3. Legacy standalone board documents are retired from active paths and moved to `.recycle-bin` with
   path-preserving structure for traceability.
4. Procurement-detail lock remains deferred to post-merge final design/BOM sweep.
