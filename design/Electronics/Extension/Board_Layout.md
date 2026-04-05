# Extension Board Layout Visualisations

**Status:** Draft
**Project:** Enigma-NG
**Author:** Enigma-NG Hardware Team
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

---

## Component Areas

```text
TOP VIEW (L1) - 4-Layer / 2oz Copper / ENIG
 _____________________________________________________________________________
|                                                                             |
|   [ J7: EXTENSION PORT IN ] <--- 16-pin 2×8 shrouded, from previous stage  |
|                                                                             |
|   [ BULK DECOUPLING ] <--- 5x 10uF X7R star/spoke near J7                  |
|                                                                             |
|   [ ROTOR INTERFACE CONNECTORS ]                                            |
|   (J1-J3: input side ERM8 male; J4-J6: output side ERF8 female)            |
|                                                                             |
|   [ JTAG BUFFER (U1) ] <--- SN74LVC2G125DCUR, TCK+TMS re-drive for output   |
|                                                                             |
|   [ DIAGNOSTIC BANK ] <--- 2x8 ENIG Gold Probe Pads                        |
|                                                                             |
|   [ J8: EXTENSION PORT OUT ] <--- 16-pin 2×8 shrouded, to next stage       |
|                                                                             |
|   [ DATA PLATE ] <--- Inverted White Silkscreen on L4                      |
|_____________________________________________________________________________|
```

---

## J7 — Extension Port IN (16-Pin 2×8)

> **Connector Definition Owner:** `Stator/Board_Layout.md — J7`.
> This board uses the mating connector on J7. See BOM for part number.
> Authoritative pinout: Pin 1 = 3V3_ENIG, Pin 2 = SYS_RESET_N, Pins 3–8 = ENC_IN[0:5],
> Pins 9–14 = ENC_OUT[0:5], Pin 15 = TDO_RETURN, Pin 16 = GND.

---

## J8 — Extension Port OUT (16-Pin 2×8)

> **Connector Definition Owner:** `Stator/Board_Layout.md — J7`.
> This board uses the mating connector on J8. Carries the same signals as J7, passed through.
> See BOM for part number.

---

## J1–J6 — Rotor Interface Connectors (ERM8/ERF8 Family, 0.8mm Pitch)

> **Connector Definition Owner:** `Rotor/Design_Spec.md §3.4`.
> J1–J3 are ERM8 male headers (input side — plug into previous rotor group's last rotor J4–J6 ERF8 outputs).
> J4–J6 are ERF8 female sockets (output side — receive next rotor group's first rotor J1–J3 ERM8 male headers).

| Ref | Side | Signal Group | Type | JLCPCB PN |
| --- | ---- | ------------ | ---- | --------- |
| J1 | Input (plugs into previous group last rotor J4) | JTAG | ERM8-005-05.0-S-DV-K-TR (10-pin, **male**) | C374877 |
| J2 | Input (plugs into previous group last rotor J5) | Power | ERM8-005-05.0-S-DV-K-TR (10-pin, **male**) | C374877 |
| J3 | Input (plugs into previous group last rotor J6) | ENC Data | ERM8-010-05.0-S-DV-K-TR (20-pin, **male**) | C374877 |
| J4 | Output (receives next group first rotor J1) | JTAG | ERF8-005-05.0-S-DV-K-TR (10-pin, female) | C7273978 |
| J5 | Output (receives next group first rotor J2) | Power | ERF8-005-05.0-S-DV-K-TR (10-pin, female) | C7273978 |
| J6 | Output (receives next group first rotor J3) | ENC Data | ERF8-010-05.0-S-DV-K-TR (20-pin, female) | C3646170 |

**Important:** ERM8/ERF8 0.8mm pitch — physically incompatible with any 2.54mm connector.
Mark clearly on silkscreen: `ERM8/ERF8 / 0.8mm / NICHT 2.54mm`.

---

## Diagnostic Bank (J9)

2×8 ENIG Gold probe pad bank for mid-stack signal validation. 2.54mm pitch. Not a separate connector;
probed directly with logic analyser clips.
