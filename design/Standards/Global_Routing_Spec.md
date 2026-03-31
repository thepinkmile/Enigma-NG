# Enigma-NG Global Routing Specification (V1.0)

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

### 3. Mechanical Grounding

* **Mounting Holes:** 3.2mm PTH for M3 screws.
* **Pattern:** Star-Burst (Radial) copper relief (8 spokes, 20-mil width) for mechanical flex.
* **Plating:** 6.0mm Exposed ENIG Gold annular ring on Top and Bottom.
* **Bonding:** Electrically tied to GND_CHASSIS for Faraday Cage continuity.

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
