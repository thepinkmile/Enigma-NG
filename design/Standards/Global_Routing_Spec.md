# Enigma-NG Global Routing Specification (V1.0)

**Status:** Draft
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

## 1. Trace & Via Geometry

* **Arcs:** All directional changes must use Full Circular Arcs (0.5mm Logic / 1.0mm Power).
* **Teardrops:** 0.5mm curved teardrops required on all High-Current (5.5A+) pads and vias.
* **Fillets:** All PCB corners and internal cutouts must feature a 2.0mm fillet (rounded corners).
* **Standard Radius:** 0.5mm for signal/logic; 1.0mm for power rails.
* **Mitres:** Sharp 45/90-degree corners are strictly prohibited to ensure signal integrity and reduce EMI.
* **Internal Layers:** 10 mil minimum width for signal traces on multi-layer boards.
* **Clearance:** 10 mil minimum spacing to reduce crosstalk and noise.
* **Grid Snap:** 0.5mm strict snap for all primary component placement and trace nodes.

## 2. Manufacturing & Mask

* **PCB Stackup:** System-wide 2oz Finished Copper (ensures zero voltage drop across links).
  * **Spec-A:** Dual-Side Assembly + Hidden/Burried Vias.
  * **Spec-B:** Single-Side Assembly (used for prototyping).
* **Mask Type:** NSMD (Non-Solder Mask Defined) for ICs/PowerPAKs; SMD for passives.
* **Expansion:** Global Solder Mask Expansion set to 3mil (0.075mm).
* **Bridge:** Minimum 4mil (0.1mm) Solder Mask Bridge between pads.
* **Thermal:** Type VII (Filled/Capped) Hexagonal Thermal Via Matrix for all high-heat zones.
* **Thermal Mesh:** Large exposed copper zones must use a 45-degree cross-hatch (10-mil trace / 10-mil gap) to prevent board warping during reflow.
* **Mask Clearance:** Global Solder Mask Expansion set to 3mil; Minimum Mask Bridge set to 4mil.
* **Mounting:** M3 PTH holes must be gold-plated (ENIG) and tied to GND_CHASSIS for Faraday cage continuity.

### 2.1. Advanced Manufacturing

* **Via-in-Pad (POFV):** Mandatory for CM5 and Samtec high-density clusters. Vias must be Epoxy Filled and Capped (IPC-4761 Type VII).
  * **High-Current Thermal Reliefs:** Standard 10-mil spokes are FORBIDDEN on 2oz Power/GND planes for 5.5A+ rails.
  * **Heavy Spokes:** All high-current via-in-pad clusters (Samtec Alpha/Beta, Buck, eFuse) MUST use 20-mil (0.5mm) wide thermal relief spokes.
  * **Pattern:** 4-spoke orthogonal pattern to ensure reliable solder reflow while maintaining massive current-carrying capacity.

### 2.2. Prototype Standards (Spec-B)

* **Component Placement:** All active and passive components (CPLDs, ICs, SMT Passives) MUST be placed on the Top Layer (L1) for the V1.0 prototype.
* **Bottom Layer (L_MAX):** Reserved strictly for Diagnostic Banks, Data Plates, and global GND_CHASSIS pours.

### 3. Mechanical Grounding

* **Mounting Holes:** 3.2mm PTH for M3 screws.
* **Pattern:** Star-Burst (Radial) copper relief (8 spokes, 20-mil width) for mechanical flex.
* **Plating:** 6.0mm Exposed ENIG Gold annular ring on Top and Bottom.
* **Bonding:** Electrically tied to GND_CHASSIS for Faraday Cage continuity.
* **EMI Landing Zones:** 10mm unmasked ENIG gold landing strips required on board edges for compression-fit cable shielding (Stator, Extension & Reflector).
* **Structural Ground:** Combine PCB mounting points with EMI zones using M3 PTH bonded to GND_CHASSIS.

### 4. Single-Point GND_CHASSIS Bond (Global Rule)

**Every board must connect its signal/power reference ground (GND) to GND_CHASSIS at exactly one point.**

* **Rule:** One and only one galvanic bridge between the GND reference plane and GND_CHASSIS per board.
  Multiple bond points create ground loops, which are a leading cause of common-mode radiated emissions and conducted susceptibility failures.
* **Placement:** The bond point must be located as close as possible to the incoming power rails
  — at the boundary between the "dirty" (external/input) side and the "clean" (internal signal) side of the board.
* **Implementation:** A dedicated 0Ω link, copper bridge, or direct via connection at the defined bond point. Mark clearly on silkscreen and schematic.
* **Per-board guidance:**
  * **Power Module:** Bond point between OR-ing diode network output and eFuse input (the clean/dirty boundary). See `Certification_Evidence.md §2.2`.
  * **All other boards:** Bond point at the power entry connector (BtB or power header), on the GND pin side, before any local decoupling.
* **Reference:** MIL-STD-461G §3.6; documented rationale in `Standards/Certification_Evidence.md §2.2`.

## 4. Branding & Identity (The "Data Plate")

To maintain a unified "Museum-Grade" look, every board must feature the V1.0 Data Plate on the **Bottom Silkscreen (B.Silkscreen)** layer.

* **Background:** Inverted solid white silkscreen rectangular block on the bottom layer.
* **Graphic:** The Enigma silhouette and "ENIGMA-NG" text, knocked out of the white block, revealing the dark green solder mask.
* **Serial Number:** A clear zone within the white block containing the string `JLCJLCJLCJLC` for the JLCPCB automated serial numbering service.
* **Metadata:** Must include `AUSGABE [Rev] V1.0` in ALL-CAPS German typewriter font.
* **Placement:** Positioned in a "Quiet Zone" on the bottom layer, away from critical test points.

## 5. Silkscreen Standards

* **Font:** All text must use the "KiCad Font" with a typewriter-style appearance.
* **Language:** Bilingual German/English (e.g., `SICHERHEITS-PROBE [Safety Probe]`).
* **Warning Labels:** High-voltage or high-energy zones must be demarcated with a 0.2mm border box.

## 6. Vias & Teardrops

These rules apply to all boards in the Enigma-NG system.

* **VIPPO (Via-in-Pad):** 0.2mm Drill / 0.45mm Diameter (Plugged & Capped).
* **Standard Via:** 0.3mm Drill / 0.6mm Diameter (Staggered zigzag pattern).
  * **Spec-A (Premium):** Blind/Buried Vias (L1-L3) and Back-drilling for all 5Gbps differential pairs to eliminate stubs.
  * **Spec-B (Standard):** Through-hole Vias using POFV (Via-in-Pad). Vias MUST be Epoxy Filled and Capped (IPC-4761 Type VII) to provide a flat solderable surface for CM5/Samtec pads.
* **Teardrops:** Enabled on all signal and power pads to reduce stress and impedance steps.
* **Copper:** 2oz Finished Copper (L1-L6 on 6-layer boards; L1-L4 on 4-layer boards).
* **Finish:** ENIG (Electroless Nickel Immersion Gold) mandatory for 0.4mm pitch integrity (all BtB connector pads and diagnostic probe loops).
