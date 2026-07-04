# Design Modification Specification: Cypher Engine + `GND_CHASSIS` ring definition

**Status:** In Discussion — no design changes made yet  
**Todo ID:** `extension-mechanical-usage`  
**Opened:** 2026-05-17  
**Last Updated:** 2026-06-08  

---

## Purpose

This document is a pre-design discussion space. The user has a set of changes in mind that will significantly reshape how the Extension board and the boards it interfaces with physically interact.
All design implications, component requirements, and open questions should be captured here before any changes are made to design specifications or schematics.

**No design files should be modified until this discussion reaches a clear decision point and explicit implementation approval is given.**

---

## Known Scope

### New Boards Being Defined

| New Board Name | Description | Source Circuits |
| --- | --- | --- |
| **Cypher Board** | Central backplane board. Replaces STA + REF. Rotor mini-stacks attach to it. Also absorbs the JTAG Module (from CTL). BtB connections to CTL, Stack-Input, Stack-Output, and Input-Cypher Board or Output-Cypher Board. 4 ENC modules via Hirose-style BtB for plugboard wiring via spade tab connectors on back. 6-layer stackup. | STA circuits + REF circuits + JM circuits (from CTL) |
| **Stack-Input Board** | Input-side board of the Rotor Mini-Stack. **Front = right edge** (1 male stacking connector: -1mm vertically from centre). **Back = left edge** (1 female stacking connector: same positions). Input mating connectors to first ROT board. AM circuits native. Receives **5V_MAIN + 3V3_ENIG** via stacking connectors. Carries ribbon cable IDC for ENC_DATA. | EXT input-side circuits + AM circuits |
| **Stack-Output Board** | Output-side board of the Rotor Mini-Stack. **Front = left edge** (1 male stacking connector:  +1mm vertically from centre). **Back = right edge** (1 female stacking connector: same positions). Output mating connectors from last ROT board. Receives **3V3_ENIG only** via stacking connectors. Carries ribbon cable IDC for ENC_DATA. | EXT output-side circuits |
| **Stack-Baseboard** | Passive bottom mounted base plate for interconnects between Stack-Input and Stack-Output (1 right-angle IDC connector to Stack-Output, 1 shrouded male header to Stack-Input ) | New design |
| **Stack-Blanking Board** | Termination board. **Male connectors** matching all female positions (Stack-Input back + Stack-Output back). Terminates the last mini-stack in the chain. Can also connect directly to Cypher Board female connectors for transport/testing without mini-stacks fitted. Passive or near-passive. | New design |
| **Input-Cypher Board** | Essentially the keyboard. 1 ENC module via Hirose-style BtB. Mechanical keyboard buttons on opposite face. BtB connection to Cypher Board. Chains with Output-Cypher Board in either order. | New design; ENC becomes module |
| **Output-Cypher Board** | Essentially the lightboard. 1 ENC module via Hirose-style BtB. LEDs on opposite face. BtB connection to Cypher Board. Chains with Input-Cypher Board in either order. | New design; ENC becomes module |

### Rotor Mini-Stack

The Rotor Mini-Stack is the assembly unit consisting of:

- **ROT boards** (5 per mini-stack — one per rotor position in the stack; maximum 6
  mini-stacks in the system = 30 rotor positions total)
- **Stack-Baseboard** (fitted to the base of the mini-stack to passivley connect Stack-Input and Stack-Output)
- **Stack-Blanking Board** (fitted to the rear of the last mini-stack only — terminates the
  chain; passivley routes TTD_RETURN and ENC_DATA inputs & outputs for Reflector)
- **Stack-Input Board** (front: connects to Cypher Board or previous mini-stack rear; rear:
  connects to next mini-stack or blanking board; surface Samtec connectors; connect to the
  input mating connectors of first ROT board)
- **Stack-Output Board** (rear: connects to next mini-stack or blanking board; surface Samtec
  connectors: connect to output mating connectors from last ROT board; front: connects to
  previous mini-stack rear or Cypher Board)

#### Stacking Connector Topology

```text
               [ Stack-Blanking ]
                /               \
               /                 \
   Stack-Input BACK             Stack-Output BACK
    (right edge)                 (left edge)
          |       ←-- ROT x5 --→      |
   [Stack-Input]                  [Stack-Output]
          |  ←---- Stack-Base ----→   |
   Stack-Input FRONT            Stack-Output FRONT
    (left edge)                  (right edge)
               \                 /
                \               /
             (STA side)    (REF side)
                  [  Cypher  ]
```
