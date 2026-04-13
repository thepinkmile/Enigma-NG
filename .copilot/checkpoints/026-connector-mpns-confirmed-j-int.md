**ENC_B[0:2]** are the 3-bit position output from the Track B capacitive sensor (FDC2114 U3) on Board B — they carry the lower track's encoder reading back to Board A's CPLD to form the complete 6-bit position (3 bits Track A + 3 bits Track B). They only carry data for the N=64 rotor variant.

The JTAG interleaved-GND pinout (TCK, GND, TMS, GND, TDO) is a good call — consistent with the convention used on the 10-pin JTAG chain throughout the rest of the design. And 4× 3V3_ENIG + 1× GND for H_PWR is clean.

Revised pinout proposal:

| Header | Pins | Signals |
|--------|------|---------|
| H_SW3 (7-pin) | 7 | SW3[0], SW3[1], SW3[2], SW3[3], SW3[4], SW3[5], GND |
| H_PWR (5-pin) | 5 | 3V3_ENIG ×4, GND |
| H_JTAG (5-pin) | 5 | TCK, GND, TMS, GND, TDO |
| H_I2C (5-pin) | 5 | SDA, SCL, ENC_B[0], ENC_B[1], ENC_B[2] |

22 pins total ✓. H_I2C carries both I²C (for the FDC2114 on Board B) and the ENC_B readback together, which makes sense as they're all associated with U3 on Board B.

---

<overview>
This session is a master parts list verification for the Enigma-NG hardware project. The user is manually confirming every component MPN and supplier PN (DigiKey/Mouser/JLCPCB) and the agent applies all corrections to the design documents. The primary work this segment covered: resolving two pre-existing markdownlint warnings, confirming Items C (CTS DIP switch), E (Amphenol 26-pin header), F (Adam Tech 16-pin header), G/H (Adam Tech JDB hat-headers with corrected male/female orientation), and beginning the redesign of Item D (Rotor J_INT internal interconnect).
</overview>

<history>

1. **Markdownlint warnings resolved (User_Manual.md:134 and Global_Routing_Spec.md:72)**
   - User_Manual.md: Stale Laird CM5022 reference removed entirely (no "original" part exists at this design stage)
   - Global_Routing_Spec.md: Bulk Entry Bank Rule exception split into indented sub-bullet
   - Committed `0ec9d90` — zero lint warnings now across all docs

2. **CTS 219-series DIP switch datasheet committed**
   - Datasheet `CTS-Switches-DIP-219-Series-Datasheet.pdf` had been omitted from the previous commit (`d95f07d`) that applied the DIP switch PNs — committed separately as `15d8bb3`

3. **Item E: Amphenol T821126A1S100CEU — 26-pin 2×13 2.54mm shrouded box header**
   - Used on: Stator J4/J5/J6, Encoder J2
   - JLCPCB: C3013501; RS-Online: 832-3503 (noted in description field, not Mouser column)
   - No DigiKey or Mouser PN available; JLCPCB direct stock

4. **Item F: Adam Tech BHR-16-VUA — 16-pin 2×8 2.54mm shrouded box header**
   - Used on: Stator J7, Reflector J4, Extension J7/J8
   - Mouser 737-BHR-16-VUA, DigiKey 2057-BHR-16-VUA-ND, JLCPCB C17692295
   - Committed `7495a8d` (items E and F together)

5. **Items G/H: JDB hat-headers — orientation correction + Adam Tech parts**
   - Previous spec had male headers on Controller and female on JDB — user confirmed this was wrong
   - Correct orientation: **male on JDB** (plugs into Controller), **female on Controller**
   - JDB J1 (5-pin INPUT): Adam Tech PH1-05-UA — Mouser 737-PH1-05-UA, DigiKey 2057-PH1-05-UA-ND, JLCPCB C5374051
   - Controller J_JDB_PWR (female): Adam Tech RS1-05-G — Mouser 737-RS1-05-G, DigiKey 2057-RS1-05-G-ND, JLCPCB C3321119
   - JDB J2 (10-pin JTAG OUTPUT): Adam Tech PH1-10-UA — Mouser 737-PH1-10-UA, DigiKey 2057-PH1-10-UA-ND, JLCPCB C3330527
   - Controller J_JDB_JTAG (female): Adam Tech RS1-10-G — Mouser 737-RS1-10-G, DigiKey 2057-RS1-10-G-ND, JLCPCB C3320525
   - Datasheets `ph1-xx-ua-data-sheet.pdf` and `rs1-xx-g-datasheet.pdf` added
   - Committed `373a93e`

6. **Item D: Rotor J_INT redesign — in progress**
   - Original spec: single 2×11 (22-pin) keyed IDC box header — Würth 61201221721 (MPN does not exist)
   - User proposed redesign: 4 separate single-row headers totalling 22 pins
   - Initial proposal: 2×1×5 + 2×1×6 = 22 — rejected because 6-pin variant not available at JLCPCB
   - **Agreed approach: 3×1×5 + 1×1×7 = 22 pins**
   - **Keying mechanism:** mixed gender on same board — Board A has 2× female 5-pin + 1× male 5-pin + 1× male 7-pin; Board B has inverse. 7-pin unique footprint makes incorrect assembly geometrically impossible
   - **Mechanical benefit:** 4 distributed connection points add rigidity to the two-board rotor assembly
   - **Signal grouping (finalised):**

| Header | Size | Signals |
|--------|------|---------|
| H_SW3 | 1×7 | SW3[0], SW3[1], SW3[2], SW3[3], SW3[4], SW3[5], GND |
| H_PWR | 1×5 | 3V3_ENIG ×4, GND |
| H_JTAG | 1×5 | TCK, GND, TMS, GND, TDO |
| H_I2C | 1×5 | SDA, SCL, ENC_B[0], ENC_B[1], ENC_B[2] |

   - **ENC_B[0:2] clarification:** 3-bit position output from Track B FDC2114 (U3) on Board B — passed to Board A CPLD for complete 6-bit position (N=64 only); grouped with I²C since both are associated with U3 on Board B
   - **H_JTAG interleaved GND:** TCK, GND, TMS, GND, TDO — consistent with JTAG shielding convention used throughout project
   - **Parts confirmed:** PH1-07-UA (Mouser 737-PH1-07-UA, DigiKey 2057-PH1-07-UA-ND, JLCPCB C3331618); RS1-07-G (Mouser 737-RS1-07-G, DigiKey 2057-RS1-07-G-ND, JLCPCB C3321543)
   - **NOT YET COMMITTED** — design spec update pending

</history>

<work_done>

Commits this segment:
- `0ec9d90` — Fix remaining markdownlint MD013 warnings
- `15d8bb3` — Add CTS 219-series DIP switch datasheet (missed from previous commit)
- `7495a8d` — Items E & F: shrouded IDC header MPNs
- `373a93e` — Items G & H: Adam Tech PH1/RS1 hat-header pairs

Files modified (all committed):
- `design/Guides/User_Manual.md` — removed stale Laird reference
- `design/Standards/Global_Routing_Spec.md` — Bulk Entry Bank Rule split to sub-bullet
- `design/Electronics/Stator/Design_Spec.md` — J4-J6 (Amphenol), J7 (Adam Tech BHR-16-VUA)
- `design/Electronics/Encoder/Design_Spec.md` — J2 (Amphenol T821126A1S100CEU)
- `design/Electronics/Reflector/Design_Spec.md` — J4 (BHR-16-VUA)
- `design/Electronics/Extension/Design_Spec.md` — J7/J8 (BHR-16-VUA)
- `design/Electronics/JTAG_Daughterboard/Design_Spec.md` — J1/J2 male pin headers (PH1 series), DR-JDB-09 updated
- `design/Electronics/Controller/Design_Spec.md` — J_JDB_PWR/JTAG female sockets (RS1 series), BOM rows added
- `design/Electronics/Consolidated_BOM.md` — all above reflected; datasheet links added; §6 note updated
- `design/Datasheets/CTS-Switches-DIP-219-Series-Datasheet.pdf` — added
- `design/Datasheets/ph1-xx-ua-data-sheet.pdf` — added
- `design/Datasheets/rs1-xx-g-datasheet.pdf` — added

**In progress (NOT YET APPLIED):**
- Item D: Rotor J_INT redesign — full spec update across Rotor/Design_Spec.md, Rotor/Board_Layout.md, Consolidated_BOM.md

**markdownlint status:** Zero warnings across all docs.

</work_done>

<technical_details>

**Adam Tech PH1/RS1 series — hat-header convention:**
- PH1-xx-UA = male pin header (xx = pin count); THT vertical 2.54mm
- RS1-xx-G = female socket (xx = pin count); THT vertical 2.54mm
- Convention in this project: male on sub/daughterboard (JDB, rotor Board B), female on main/receiving board (Controller, rotor Board A)
- Both series use same footprint for each pin count → confirmed mating pairs

**J_INT redesign — keying via mixed gender:**
- 3×5-pin + 1×7-pin = 22 pins (same signal count as original 2×11)
- Board A: H_SW3=PH1-07-UA (male), H_PWR=RS1-05-G (female), H_JTAG=RS1-05-G (female), H_I2C=PH1-05-UA (male)
- Board B: H_SW3=RS1-07-G (female), H_PWR=PH1-05-UA (male), H_JTAG=PH1-05-UA (male), H_I2C=RS1-05-G (female)
- 7-pin unique footprint prevents rotation error; mixed gender prevents board inversion

**ENC_B[0:2]:**
- 3-bit Track B capacitive encoder output from FDC2114 U3 on Board B → to Board A CPLD
- Only populated/used for N=64 rotor variant (not N=26)
- Transmitted via J_INT H_I2C header alongside I²C (SDA/SCL) since both relate to Board B U3

**JTAG interleaved GND convention:**
- H_JTAG pinout: TCK, GND, TMS, GND, TDO — consistent with all other JTAG connections in the design
- This matches the 10-pin JTAG chain standard used on JDB J2 and LINK-BETA

**Stale MPNs to never reappear:**
- Würth 61300511021, Würth 61301011021 (replaced by RS1-05-G / RS1-10-G on Controller)
- Molex 22-23-2261 (replaced by Amphenol T821126A1S100CEU)
- Molex 22-23-2161 (replaced by Adam Tech BHR-16-VUA)
- Würth 61201221721 (J_INT — never existed; being replaced by 4-header arrangement)
- JLCPCB C50950, C2337 (old generic female header PNs for JDB — replaced by PH1 series)

**RS-Online handling:**
- RS-Online PNs (e.g. 832-3503 for Amphenol T821126A1S100CEU) go in the description/value field, NOT in the Mouser column
- Mouser column gets `—` when no Mouser stock exists

**markdownlint:**
- Zero warnings now (all pre-existing issues resolved)
- Run via: `$env:PATH = ...; .\node_modules\.bin\markdownlint.cmd "design/**/*.md" --fix` then without --fix

</technical_details>

<important_files>

- `design/Electronics/Rotor/Design_Spec.md`
  - J_INT spec at §3.4 (~lines 393–432): full 22-pin pinout, assembly notes, ⚠️ warning — **all needs replacing** with 4-header redesign
  - Board A BOM (~line 471) and Board B BOM (~line 490): J_INT rows — both need updating
  - SW1/SW2/SW3 (lines 480–492): already updated with 219-6LPSTR PNs

- `design/Electronics/Rotor/Board_Layout.md`
  - Lines 18, 49, 66, 78, 109, 121: all reference "J_INT: keyed IDC 2×11" — need updating to 4-header arrangement

- `design/Electronics/Consolidated_BOM.md`
  - Line 104: Würth 61201221721 ⚠️ row — needs replacing with 4 new Adam Tech rows
  - §11 datasheet section: needs PH1-07-UA / RS1-07-G entries added
  - Component count table: needs rows for PH1-07-UA (ROT=4, total=120) and RS1-07-G (ROT=4, total=120)

- `design/Electronics/JTAG_Daughterboard/Design_Spec.md`
  - Already updated this segment — J1/J2 now correctly male PH1 headers
  - BOM rows lines 180–181: already correct

- `design/Electronics/Controller/Design_Spec.md`
  - J_JDB_PWR/JTAG sections (~lines 282–302): already updated to RS1 female sockets
  - BOM J_JDB_PWR/JTAG rows: already added after J_FAN

</important_files>

<next_steps>

**Immediate — in progress:**

**Item D: Apply J_INT redesign to Rotor docs**

Signal allocation (confirmed):
| Header | Gender Board A | Gender Board B | Pins | Signals |
|--------|---------------|---------------|------|---------|
| H_SW3 | PH1-07-UA (male) | RS1-07-G (female) | 7 | SW3[0], SW3[1], SW3[2], SW3[3], SW3[4], SW3[5], GND |
| H_PWR | RS1-05-G (female) | PH1-05-UA (male) | 5 | 3V3_ENIG×4, GND |
| H_JTAG | RS1-05-G (female) | PH1-05-UA (male) | 5 | TCK, GND, TMS, GND, TDO |
| H_I2C | PH1-05-UA (male) | RS1-05-G (female) | 5 | SDA, SCL, ENC_B[0], ENC_B[1], ENC_B[2] |

Parts (all confirmed):
- PH1-05-UA: Mouser 737-PH1-05-UA, DigiKey 2057-PH1-05-UA-ND, JLCPCB C5374051 (already in BOM)
- RS1-05-G: Mouser 737-RS1-05-G, DigiKey 2057-RS1-05-G-ND, JLCPCB C3321119 (already in BOM)
- PH1-07-UA: Mouser 737-PH1-07-UA, DigiKey 2057-PH1-07-UA-ND, JLCPCB C3331618 (new)
- RS1-07-G: Mouser 737-RS1-07-G, DigiKey 2057-RS1-07-G-ND, JLCPCB C3321543 (new)

Files to update:
1. `Rotor/Design_Spec.md`: Replace J_INT section (~lines 393–432) with 4-header spec + new pinout table; update Board A BOM (~471) and Board B BOM (~490)
2. `Rotor/Board_Layout.md`: Update all 6 references to "J_INT: keyed IDC 2×11"
3. `Consolidated_BOM.md`: Replace Würth 61201221721 row (line 104) with 2 new rows (PH1-07-UA and RS1-07-G, ROT=4 each = 120 per type); add datasheet links in §11

**Then:**
- Item J: PM SW1 — Marquardt 1800 illuminated power switch (RGB LED) — was deferred, now to be picked up
- Passive components from #28 onwards
- Rotor single-side JLCPCB constraint resolution
- Rotor detailed design review cycle (2 clean passes)
- KiCad project setup

</next_steps>