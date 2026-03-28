# Enigma-NG Global Routing Specification (V1.0)

### 1. Trace Geometry
*   **Arcs:** All directional changes must use Full Circular Arcs.
*   **Standard Radius:** 0.5mm for signal/logic; 1.0mm for power rails.
*   **Mitres:** Sharp 45/90-degree corners are strictly prohibited to ensure signal integrity and reduce EMI.

### 2. Physical Constraints
*   **Internal Layers:** 10 mil minimum width for signal traces on multi-layer boards.
*   **Clearance:** 10 mil minimum spacing to reduce crosstalk and noise.
*   **Teardrops:** 0.5mm curved teardrops required on all High-Current (5.5A) pads and vias.
*   **Board Edge:** All PCB corners and internal cutouts must feature a 2.0mm fillet (rounded corners).
