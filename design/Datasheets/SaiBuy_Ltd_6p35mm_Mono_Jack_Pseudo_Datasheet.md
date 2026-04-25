# SaiBuy.Ltd 6.35 mm Mono Switched Jack Socket — Pseudo Datasheet

**Status:** Pseudo datasheet derived from marketplace listing metadata  
**Project:** Enigma-NG  
**Author:** Izzyonstage & GitHub Copilot  
**Version:** v.0.1.0
**Last Updated:** 2026-04-19  
**Source Listing:** eBay item `334364197440`  
**Seller:** `SaiBuy.Ltd`  
**Brand Shown on Listing:** `Unbranded`  
**Listing Title:** `3x 6.35mm 1/4" Mono Audio Socket Jack Female Connector Panel Mount Solder !`  
**Original URL:** <https://www.ebay.co.uk/itm/334364197440>

---

## 1. Purpose

This document captures the technical details that could be recovered from the marketplace listing
for the purchased plugboard jack sockets used by Enigma-NG. It is **not** a manufacturer-issued
datasheet and must be treated as a project-side reference only.

Use this part only where a marketplace-sourced plugboard jack is acceptable and where no stable
catalogue MPN or formal manufacturer datasheet has been established.

---

## 2. Intended Enigma-NG Use

- **Assembly:** `design/Mechanical/Plugboard_Assembly/Design_Spec.md`
- **Board interface:** `design/Electronics/Encoder/Design_Spec.md`
- **Function:** Plugboard / Stecker panel jack socket
- **System quantity:** 64 sockets total
- **Electrical use in Enigma-NG:** three-terminal switched mono jack
  - **Tip:** `BT1`-`BT64` decode-half signal path
  - **Switch (N/C):** same node as Tip; shorts Switch to Sleeve when no plug is inserted
  - **Sleeve:** `BT65`-`BT128` encode-half input path

---

## 3. Observed Listing Specifications

The following values were extracted directly from the eBay listing HTML:

| Parameter | Value from listing |
| :--- | :--- |
| Listing type | Buy It Now |
| Condition | New |
| Brand | Unbranded |
| Type | Audio Splitter/Switcher |
| Connector style | 6.35 mm (1/4 in) Jack Female |
| Features | Switched, Mono |
| Mounting wording in title | Panel Mount |
| Termination wording in title | Solder |
| Connection split/duplication | None (1:1) |
| Cable length | Not Applicable |
| Gauge | Not Applicable |
| Country of origin | China |
| Warranty | 1 year |
| Pack quantity | 3 pieces per lot |
| Seller location | Bradford, West Yorkshire, United Kingdom |

Listing title text:

> 3x 6.35mm 1/4" Mono Audio Socket Jack Female Connector Panel Mount Solder !

---

## 4. Enigma-NG Integration Notes

| Attribute | Enigma-NG usage note |
| :--- | :--- |
| Jack type | Treat as a switched mono 6.35 mm panel jack |
| Wiring | Harness back to Encoder blade terminals `BT1`-`BT128` |
| Normal state | N/C switch contact provides identity passthrough when no Stecker plug is inserted |
| Plugboard role | Forms the physical plugboard matrix interface for Decode Half to Encode Half bridging |
| Procurement | Purchased marketplace part; no stable manufacturer MPN currently recorded |

---

## 5. Known Unknowns / Unverified Parameters

The listing did **not** provide a trustworthy manufacturer datasheet for these items:

- Panel cutout diameter
- Thread / bushing dimensions
- Exact terminal numbering and pinout drawing
- Contact voltage / current rating
- Contact material and plating
- Insulation resistance / dielectric withstand
- Mechanical life / insertion cycle rating
- Operating temperature range
- Exact manufacturer name and part number
- Compliance data (RoHS, REACH, UL, etc.)
- Dimensional tolerances

These values remain **unverified** and should not be invented elsewhere in the design docs.

---

## 6. Procurement and Risk Notes

- This is a **single-source marketplace part** rather than a catalogue component with a stable MPN.
- The listing identifies the item only as **Unbranded**, so long-term repeatability is uncertain.
- Extra spares should be retained because the exact physical variant may drift over time.
- If the plugboard hardware is ever redesigned for long-term maintainability, this part should be
  replaced with a catalogue switched mono jack that has a formal manufacturer datasheet.

---

## 7. Document Status

This pseudo datasheet is sufficient to preserve the currently known connector style and marketplace
listing metadata for the purchased Enigma-NG plugboard jack sockets. It does **not** replace a
real manufacturer datasheet.
