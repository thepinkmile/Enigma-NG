# PAS-PWR-V1.0: Power Module Acceptance Specification

**Status:** Draft
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-20

## ⚠️ HINWEIS: THERMISCHE GRENZFLÄCHE (Thermal Interface)

* The exposed ENIG zones can become extremely hot under full load (>5A).
* **PROCEDURE:** Gelid-GP thermal pad MUST be applied before live testing.

## 1. Bare Board "Cold" Tests (Pre-Power)

* [ ] **Chassis Isolation:** Confirm >1MΩ resistance between the 15V Rail and the Aluminium Tray.*
* [ ] **TCO Continuity:** Confirm 0Ω across the Bourns AC72 Thermal Cutoff pads.
* [ ] **Ground Bridge:** Confirm 0Ω across the 15A GND_CHASSIS diagnostic shunts.
* [ ] **Hex-Matrix:** Visual check of Type VII via-capping on L4 (must be mirror-flat).

## 2. Live Input Verification

* [ ] **PoE Auxiliary Feed:** Apply 48V to the Controller Ethernet / PoE entry; verify regulated
  `VIN_POE_12V` is present at Power Module dock `J2` and reaches the PM OR-ing / eFuse input path.
* [ ] **USB-C PD:** Connect 15V PD source; verify negotiated voltage and stable rail.
* [ ] **Battery:** Connect 14.4V battery; verify SMBus pull-ups are active.

## 3. Logic & Handshake

* [ ] **Safety Glow:** Confirm Amber LED illuminates at >5.1V and extinguishes at ~5.0V.
* [ ] **Discharge:** Ensure < 2V at Safety Probes before handling board.
* [ ] **Logic Ready:** Confirm Green "LOGIK-BEREIT" LED illuminates only when 5V/3.3V rails are stable.
* [ ] **Handshake:** Verify `PWR_GD` on PM dock `J3` goes HIGH (>3.0V).
* [ ] **UPS Hold-time:** Load 15W; pull power; verify ≥33.5s uptime before dropout.

## 4. Header & Coupon Verification

* [ ] **Dock Orientation:** Confirm `J1/J2/J3` are fitted in the correct keyed orientation and align
  cleanly with the Controller receptacles.
* [ ] **Straight Alignment:** Verify dock headers are vertical and coplanar to prevent blind-mate
  binding during PM insertion.
* [ ] **Adhesive Zone:** Confirm RTV Silicone 'KLEBER-ZONE' is free of solder mask for maximum bond.

## 5. Pi-Proxy Validation

* [ ] **Handshake:** Connect the Controller / CM5 assembly via the PM dock and USB-C service power path.
* [ ] **PD Check:** Verify 5V/5A negotiation via `vcgencmd get_throttled`.
* [ ] **Telemetry:** Verify I2C communication with TPS25751 PD Emulator.

## 6. V-Score & Coupon Inspection

* [ ] **TRENNLINIE:** Verify dashed silkscreen alignment with V-groove.
* [ ] **Isolation:** Confirm zero conductivity across the snap-line post-break.
