# Enigma-NG Global Routing Specification (V1.0)

## 1. Trace & Via Geometry

* **Arcs:** All directional changes must use Full Circular Arcs (0.5mm Logic / 1.0mm Power).
* **Teardrops:** 0.5mm curved teardrops required on all High-Current (5.5A) pads and vias.
* **FBoard Edge:** All PCB corners and internal cutouts must feature a 2.0mm fillet (rounded corners).
* **Standard Radius:** 0.5mm for signal/logic; 1.0mm for power rails.
* **Mitres:** Sharp 45/90-degree corners are strictly prohibited to ensure signal integrity and reduce EMI.
* **Internal Layers:** 10 mil minimum width for signal traces on multi-layer boards.
* **Clearance:** 10 mil minimum spacing to reduce crosstalk and noise.

## 2. Branding & Identity (The "Data Plate")

To maintain a unified "Museum-Grade" look, every board must feature the V1.0 Data Plate on the **Bottom Silkscreen (B.Silkscreen)** layer.

* **Background:** A solid white silkscreen rectangular block.
* **Graphic (Knockout):** The Enigma silhouette and "ENIGMA-NG" text must be "knocked out" of the white block, revealing the dark green solder mask.
* **Serial Number:** A clear zone within the white block containing the string `JLCJLCJLCJLC` for the JLCPCB automated laser-etching service.
* **Metadata:** Must include `AUSGABE [Rev] V1.0` in ALL-CAPS German typewriter font.
* **Placement:** Positioned in a "Quiet Zone" on the bottom layer, away from critical test points.

## 3. Silkscreen Standards

* **Font:** All text must use the "KiCad Font" with a typewriter-style appearance.
* **Language:** Bilingual German/English (e.g., `SICHERHEITS-PROBE [Safety Probe]`).
* **Warning Labels:** High-voltage or high-energy zones must be demarcated with a 0.2mm border box.
