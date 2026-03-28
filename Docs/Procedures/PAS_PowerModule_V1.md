# PAS-PWR-V1.0: Power Module Acceptance Specification

### 1. Bare Board "Cold" Tests (Pre-Power)
- [ ] **Chassis Isolation:** Confirm >1MΩ resistance between the 15V Rail and the Aluminium Tray.
- [ ] **TCO Continuity:** Confirm 0Ω across the Bourns AC72 Thermal Cutoff pads.
- [ ] **Ground Bridge:** Confirm 0Ω across the 15A GND_CHASSIS diagnostic shunts.
- [ ] **Hex-Matrix:** Visual check of Type VII via-capping on L4 (must be mirror-flat).

### 2. Live Input Verification
- [ ] **PoE+ Entry:** Apply 48V to RJ45; verify 15V at the eFuse input.
- [ ] **USB-C PD:** Connect 15V PD source; verify negotiated voltage and stable rail.
- [ ] **Battery:** Connect 14.4V battery; verify SMBus pull-ups are active.

### 3. Logic & Handshake
- [ ] **Safety Glow:** Confirm Amber LED illuminates at >5.1V and extinguishes at ~5.0V.
- [ ] **Logic Ready:** Confirm Green "LOGIK-BEREIT" LED illuminates only when 5V/3.3V rails are stable.
- [ ] **Handshake:** Verify PWR_GD signal (Samtec Pin 26) goes HIGH (>3.0V).
- [ ] **UPS Hold-time:** Load 5W; pull power; verify >10s uptime before dropout.
