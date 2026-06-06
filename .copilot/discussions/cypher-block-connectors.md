# Multi-Board Chassis Interconnect & Grounding Specification

## 1. Physical Architecture & System Constraints

This document specifies the electrical, mechanical, and electromagnetic compatibility (EMC) routing requirements for a structured four-board card cage chassis. The system establishes a rigid multi-planar geometric frame consisting of a Backboard, a Front Board, a Left Side Board, and a Right Side Board.

### 1.1 Structural Configuration & Mounting Planes
*   **Backboard & Front Board (Vertical Plane):** Mounted parallel to one another. The Backboard houses vertical female receptacles; the Front Board houses vertical male plugs.
*   **Side Boards (Perpendicular / Right-Angle Plane):** Mounted perpendicular to the front and back planes. The Left Side Board handles two low-density links; the Right Side Board handles two high-density links.
*   **Edge Routing Parameters:** 
    *   **Back-Facing Edge:** Populated with right-angle male plugs that slide directly into the Backboard's vertical female receptacles.
    *   **Front-Facing Edge:** Populated with right-angle female receptacles that receive the Front Board's vertical male plugs.

### 1.2 Mechanical Envelope & Clearance Constraints
*   **Enclosure Profile:** Structural outer protective shell walls feature a thickness of **1.2 mm**.
*   **Internal Air Gap:** An explicit **0.8 mm clearance margin** is maintained between the outer lip of the internal PCB layer boundaries and the inner face of the enclosure casing.
*   **Total Mechanical Offset:** The combined structural gap from the raw board edge profile to the exterior flush mating face is exactly **2.0 mm**.
*   **Flush Interface Requirements:** Female receptacles must sit completely flush against the exterior of the enclosure cutouts. Male terminal arrays must extend completely across the 2.0 mm mechanical air gap to achieve proper mating depth.

---

## 2. Connector Selection & Optimization (Consolidated BOM)

The system standardizes entirely on the **Samtec Q Strip® High-Speed Mezzanine Series** on an ultra-fine **0.635 mm (0.025") pitch**. This system eliminates traditional bulky header designs, introduces asymmetrical polarization features to prevent inverse card assembly in the field, and features an integrated heavy-gauge structural ground plane blade.

### 2.1 Current Handling Capacities
*   **Signal Contacts:** Rated for approximately 1.8 A to 2.0 A of continuous current per pin.
*   **Integral Ground Blade Wedge:** Rated for **over 23 Amps** of continuous current.
*   **Power Rail Mapping:** To support the 2 A main power rails safely, signal lines are cross-coupled. Spreading the 2 A load symmetrically across multiple adjacent pins reduces thermal stress and minimizes localized trace voltage drops.

### 2.2 System Bill of Materials (50-Position & 25-Position Standardization)

To optimize inventory, minimize minimum-order costs, and streamline automated assembly lines, the chassis drops the previous four-connector layout down to two standard sizes:

#### Set A: High-Density Node (50 Signal Pins Total, 2x25 Dual-Row Matrix + Ground Blade)
*   **Backboard (Vertical Female Socket):** `QSS-050-01-L-D-A-GP` (Features integrated `-GP` protective alignment guide-shrouds to handle blind assembly vectors).
*   **Front Board (Vertical Male Terminal):** `QTS-050-01-L-D-A` (Standardizes on **Lead Style -01**, resulting in a uniform, rigid **5.00 mm parallel board-to-board stack height**).
*   **Side Board Back Edge (Right-Angle Male Plug):** `QTS-050-01-L-D-RA-WT` (Features `-WT` welded mechanical anchoring tabs).
*   **Side Board Front Edge (Right-Angle Female Receptacle):** `QSS-050-01-L-D-RA-WT` (Features `-WT` welded mechanical anchoring tabs).

#### Set B: Low-Density Node (25 Signal Pins Total, 2x12+1 Matrix + Ground Blade)
*   **Backboard (Vertical Female Socket):** `QSS-025-01-L-D-A-GP`
*   **Front Board (Vertical Male Terminal):** `QTS-025-01-L-D-A` (Standardizes on **Lead Style -01** for uniform 5.00 mm parallel spacing).
*   **Side Board Back Edge (Right-Angle Male Plug):** `QTS-025-01-L-D-RA-WT`
*   **Side Board Front Edge (Right-Angle Female Receptacle):** `QSS-025-01-L-D-RA-WT`

### 2.3 Visual Representation of Interface Plane

~~~
    [Molded Shroud Ear]                 [Mating Lead Pin]
    ┌─────────────────┐                 ┌───────────────
    │  (Guide Hole)   │ ◄────────────── │   (Guide Post)
    ├─────────────────┤                 ├───────────────
    │ [Female Socket] │ ◄────────────── │ [Longer Pin]
~~~

---

## 3. Grounding & Shielding Architecture

The subsystem implements a strict isolation protocol between high-frequency signal returns and external static shielding lines.

### 3.1 Coplanar Signal Shielding Matrix
All individual signal pins across the 2x25 and 2x12 arrays are symmetrically interleaved with ground paths (`[Logic GND] [Signal 1] [Logic GND] [Signal 2]`).
*   **Inductance Control:** This pinout forces the physical return path loop area for every high-speed data line to approach zero as it spans the connector interface.
*   **Plane Connection:** Every ground pin maps directly to your internal **Pure Logic GND plane layers**, providing a low-impedance path directly underneath the high-speed data traces.
*   **Central Ground Blade Hookup:** The large structural central ground wedge features integrated through-hole pins. These solder directly into your internal pure logic ground planes, forming a continuous electrical mirror plane underneath the connector housing.

### 3.2 4-Edge Shielding & Faraday Protection
To isolate the system from external electro-static discharges (ESD) and radio-frequency interference, every 4-layer PCB features a continuous **`CHASSIS_GND` perimeter ring** run across all 4 copper layers.

*   **Border Width Specification:** The `CHASSIS_GND` border trace is exactly **2.5 mm wide** to enclose the structural PCB mounting holes.
*   **Isolation Moat Specification:** A complete copper-free **1.5 mm isolation moat** creates a permanent air gap between the `CHASSIS_GND` ring and the internal logic zone.
*   **Total Edge Boundary Keep-Out:** Clean signal traces and pure logic plane fills begin exactly **4.0 mm away from the raw board edge** (`2.5 mm border + 1.5 mm moat`).

~~~
 [BOARD EDGE] ──► [2.5mm CHASSIS_GND] ──► [1.5mm MOAT] ◄── 4.0mm Keep-Out ──► [INNER LOGIC ZONE]
~~~

### 3.3 Loop Antenna & Ground Loop Prevention
*   **Single-Point Star Connection:** The isolated `CHASSIS_GND` barrier network maps to the main signal reference `GND` at **exactly one single point** located exclusively on a separate, dedicated power module.
*   **The "C-Shield" Boundary Break:** To prevent circulating currents from turning the 4-edge border into a functional loop antenna, the copper ring features a literal **1.0 mm physical gap** cut through all layers on the front-facing edge of the side boards. This opens the circuit, breaking the induction path while preserving the board's ESD shielding capabilities.

---

## 4. Perpendicular Mechanical Interface Integration (The Window Method)

Because right-angle surface-mount connectors (`QSS-RA` / `QTS-RA`) are edge-mount components, their SMT signal leads must sit within the first 2.5 mm of the board lip. To prevent these pins from shorting directly into the `CHASSIS_GND` ring, the system uses an enclosure-bridged layout window.

### 4.1 The Layout Window Rules
1.  **The Copper Void:** At the exact horizontal coordinate where the side board right-angle connector sits, a window is cut completely through the 4-layer `CHASSIS_GND` ring and isolation moat (spanning approximately 40 mm to match the plastic shroud width).
2.  **Logic Extension:** Your internal **Pure Logic GND plane and high-speed data traces extend fully to the front lip of the board edge** inside this window. Your 0.635 mm SMT data pads sit directly over a continuous copper logic reference.

### 4.2 Enclosure Mechanical Bridge
1.  **Plated Anchor Points:** Plated mounting holes tied to `CHASSIS_GND` are positioned on the immediate left and immediate right sides of the connector window.
2.  **The Metal Shield Loop:** When the side card assemblies are mounted inside the chassis frame, conductive chassis brackets or internal enclosure grounding screws clamp directly onto these pads. 
3.  **Completing the Circuit:** The physical enclosure itself completes the 360° Faraday shield ring across the window, keeping your external shielding path intact without cutting off the internal signal reference planes.

~~~
       [CHASSIS_GND PLATED HOLE] ──► (Clamped to Metal Enclosure Frame)
                  │
 ┌────────────────┴────────┐              ┌────────────────────────┐
 │   PCB CHASSIS_GND Ring  │              │  PCB CHASSIS_GND Ring  │
 ├─────────────────────────┤  [OPEN GAP]  ├────────────────────────┤
 │     ISOLATION MOAT      │  (No Moat)   │     ISOLATION MOAT      │
 └─────────────────────────┘ ┌──────────┐ └────────────────────────┘
                             │  Samtec  │ 
                             │  QSS-RA  │ ◄── Pure Logic GND & Traces
                             └──────────┘     Extend Fully To Edge
~~~

### 4.3 Shear Force Protection
Right-angle surface-mount pads are vulnerable to peeling forces when modules are pushed together. 
*   The system uses Samtec's **`-WT` (Weld Tab)** configurations. 
*   The large metal side brackets on the `QSS-RA` and `QTS-RA` connectors are soldered into wide, unplated anchor pads on the edge of the board. This transfers 100% of the mechanical insertion and removal stress directly into the fiberglass core of the 4-layer PCB, protecting your fine-pitch signal leads from trace fatigue or shearing during assembly.
