# Extension Board Layout Visualisations

**Status:** Draft
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

---

## Component Areas

```text
TOP VIEW (L1) - 4-Layer / 2oz Copper / ENIG
 _____________________________________________________________________________
|                                                                             |
|   [ J1: EXTENSION PORT IN ] <--- 16-pin 2×8 shrouded, from previous stage  |
|                                                                             |
|   [ BULK DECOUPLING ] <--- 5x 10uF X7R star/spoke near J1                  |
|                                                                             |
|   [ ROTOR INTERFACE CONNECTORS ] <--- ERF8 female sockets (0.8mm pitch)      |
|   (J3-J5: input side; J6-J8: output side — see Design_Spec §2)               |
|                                                                             |
|   [ JTAG BUFFER (U1) ] <--- SN74LVC2G125DCUR, TCK+TMS re-drive for output   |
|                                                                             |
|   [ DIAGNOSTIC BANK ] <--- 2x8 ENIG Gold Probe Pads                        |
|                                                                             |
|   [ J2: EXTENSION PORT OUT ] <--- 16-pin 2×8 shrouded, to next stage       |
|                                                                             |
|   [ DATA PLATE ] <--- Inverted White Silkscreen on L4                      |
|_____________________________________________________________________________|
```

---

## J1 — Extension Port IN (16-Pin 2×8)

> **Connector Definition Owner:** `Stator/Board_Layout.md — J5`.
> This board uses the mating connector on J1. See BOM for part number.
> Authoritative pinout: Pin 1 = 3V3_ENIG, Pin 2 = SYS_RESET_N, Pins 3–8 = ENC_IN[0:5],
> Pins 9–14 = ENC_OUT[0:5], Pin 15 = TDO_RETURN, Pin 16 = GND.

---

## J2 — Extension Port OUT (16-Pin 2×8)

> **Connector Definition Owner:** `Stator/Board_Layout.md — J5`.
> This board uses the mating connector on J2. Carries the same signals as J1, passed through.
> See BOM for part number.

---

## J3–J8 — Rotor Interface Connectors (ERF8 Family, 0.8mm Pitch)

> **Connector Definition Owner:** `Rotor/Board_Layout.md — Rotor Interface Connectors`.
> This board hosts ERF8 female sockets on both sides to mate with rotor ERM8 male headers.
> Signal groups per side are defined in Design_Spec §2.

| Ref | Side | Signal Group | Type | JLCPCB PN |
| --- | ---- | ------------ | ---- | --------- |
| J3 | Input (from previous group) | JTAG | ERF8-005-05.0-S-DV-K-TR (10-pin) | C7273978 |
| J4 | Input (from previous group) | Power | ERF8-005-05.0-S-DV-K-TR (10-pin) | C7273978 |
| J5 | Input (from previous group) | ENC Data | ERF8-010-05.0-S-DV-K-TR (20-pin) | C3646170 |
| J6 | Output (to next group) | JTAG | ERF8-005-05.0-S-DV-K-TR (10-pin) | C7273978 |
| J7 | Output (to next group) | Power | ERF8-005-05.0-S-DV-K-TR (10-pin) | C7273978 |
| J8 | Output (to next group) | ENC Data | ERF8-010-05.0-S-DV-K-TR (20-pin) | C3646170 |

**Important:** ERF8 0.8mm pitch — physically incompatible with any 2.54mm connector.
Mark clearly on silkscreen: `ERF8 / 0.8mm / NICHT 2.54mm`.

---

## Diagnostic Bank (J9)

2×8 ENIG Gold probe pad bank for mid-stack signal validation. 2.54mm pitch. Not a separate connector;
probed directly with logic analyser clips.
