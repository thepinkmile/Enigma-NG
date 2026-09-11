# FT232H Rev C 3V3 VREGIN

**ID:** `jdb-ft232h-3v3-vregin`
**Status:** pending
**Category:** Electronics
**Source:** 2026-05-07
**Blocked by:** None — unblocked 2026-09-11, no longer deferred to v2.0 (part is now available)

---

## Description

FT232H Rev C supports 3.0–3.6V VREGIN, which would allow the USB-JTAG bridge (now native to the
Cypher Board's `U17`, per DEC-098/DEC-099/DEC-100 — see `Cypher/Design_Spec.md §5`) to run entirely
from `3V3_ENIG` and eliminate the `5V_USB` requirement.

## Notes

DEC-058.

USER: these have been available since 2013. DigiKey = 768-FT232HPQ-TRAY-ND, Mouser = 895-FT232HPQ-TRAY, JLCPCB = C3227934.
This should be reviewed and the update to the design made to ensure we can power via the 3V3 rail instead of the 5V rail.
Datasheet and Information PDF files added to the datasheets folder.
