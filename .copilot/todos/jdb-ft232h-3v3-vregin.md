# FT232H Rev C 3V3 VREGIN (v2.0)

**ID:** `jdb-ft232h-3v3-vregin`
**Status:** blocked
**Category:** Electronics
**Source:** 2026-05-07
**Blocked by:** None (v2.0 deferred)

---

## Description

DEFERRED TO V2.0. FT232H Rev C supports 3.0–3.6V VREGIN, which would allow JDB to run entirely from 3V3_ENIG and eliminate the 5V_USB pin from the DF40 connector. Defer until Rev C availability is confirmed. Same priority as display-addon-board.

## Notes

DEC-058.

USER: these have been available since 2013. DigiKey = 768-FT232HPQ-TRAY-ND, Mouser = 895-FT232HPQ-TRAY, JLCPCB = C3227934.
This should be reviewed and the update to the design made to ensure we can power via the 3V3 rail instead of the 5V rail.
Datasheet and Information PDF files added to the datasheets folder.
