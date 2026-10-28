"""
bom_append_new_boards.py

Appends per-board BOM rows from each board's own `Design_Spec.md §Bill of Materials` table
into `design/Electronics/Consolidated_BOM.md`, mapping each board's 12-column schema
(RefDes | Specification | MPN | Manufacturer | DigiKey PN | Mouser PN | JLCPCB PN |
Alt Supplier + PN | Notes | Footprint Available | Footprint Downloaded | Qty) onto the
Consolidated BOM's wider per-board-Qty-column schema.

Usage:
    Edit the `boards` list below (board folder name -> consolidated board code), then run:
        python .copilot/agent-scripts/bom_append_new_boards.py

Notes:
- Appended rows are NOT deduplicated against existing shared-component rows in the
  Consolidated BOM - run a manual reconciliation pass afterwards if components are shared
  across boards (e.g. common bypass caps).
- System Qty for appended rows is set equal to that board's own per-board Qty (i.e. assumes
  exactly one of that board per system). Adjust manually for boards present multiple times
  per system (e.g. Stack-Input/Output/Interposer/Blanking appear once per mini-stack, up to
  6 mini-stacks per system) or for variant-specific boards (Cypher-Input/Output/Plugboard).
- Only pulls the board's own Design_Spec.md BOM table ("common to all variants" section where
  applicable) - per-variant-only parts (e.g. Cypher-Input's 10/26/64-char variant files) are
  NOT pulled by this script and must be merged separately.
- Column removal for retiring boards is NOT handled by this script; that was a one-off
  transform performed directly against the live column set at the time. If a future board
  retirement needs the same treatment, write a similar one-off transform rather than trying
  to generalise it here, since the exact columns to remove/keep will differ each time.
"""

import re

ROOT = r"D:\_DATA_\Repositories\github\Enigma-NG\design\Electronics"
BOM_PATH = ROOT + r"\Consolidated_BOM.md"

# (board folder name under design/Electronics/, consolidated BOM column code e.g. "CYP" -> "CYP Qty")
boards = [
    ("Cypher", "CYP"),
    ("Cypher-Input", "CYPI"),
    ("Cypher-Output", "CYPO"),
    ("Cypher-Plugboard", "CYPB"),
    ("Stack-Input", "SIN"),
    ("Stack-Output", "SOUT"),
    ("Stack-Interposer", "SINT"),
    ("Stack-Blanking", "SBLK"),
]


def split_row(line):
    return [c.strip() for c in line.rstrip("\n").strip().strip("|").split("|")]


def find_bom_table(lines):
    """Locate the first '| RefDes | Specification | MPN | ...' table header line in a board's
    Design_Spec.md, following the convention established across all board docs."""
    for i, l in enumerate(lines):
        if l.startswith("| RefDes") and "Specification" in l and "MPN" in l:
            return i
    return None


def parse_board_table(board_folder):
    path = f"{ROOT}\\{board_folder}\\Design_Spec.md"
    with open(path, encoding="utf-8-sig") as f:
        lines = f.readlines()
    start = find_bom_table(lines)
    if start is None:
        raise RuntimeError(f"No BOM table found in {path}")
    data_start = start + 2  # skip header + separator row
    rows = []
    for i in range(data_start, len(lines)):
        l = lines[i]
        if not l.strip().startswith("|"):
            break
        rows.append(split_row(l))
    return rows


def main():
    with open(BOM_PATH, encoding="utf-8-sig") as f:
        bom_lines = f.readlines()

    header_idx = next(i for i, l in enumerate(bom_lines) if l.startswith("| Board (RefDes)"))
    header_parts = [c.strip() for c in bom_lines[header_idx].rstrip("\n").strip().strip("|").split("|")]
    n_cols = len(header_parts)

    sysqty_idx = header_parts.index("System Qty")
    notes_idx = header_parts.index("Notes")
    footA_idx = header_parts.index("Footprint Available")
    footD_idx = header_parts.index("Footprint Downloaded")
    mpn_idx = header_parts.index("MPN")
    dk_idx = header_parts.index("DigiKey PN")
    mouser_idx = header_parts.index("Mouser PN")
    jlc_idx = header_parts.index("JLCPCB PN")
    alt_idx = header_parts.index("Alt Supplier + PN")
    boardrefdes_idx = header_parts.index("Board (RefDes)")

    new_rows_md = []
    for folder, code in boards:
        qty_col = f"{code} Qty"
        if qty_col not in header_parts:
            raise RuntimeError(
                f"Column '{qty_col}' not found in Consolidated_BOM.md header - add it first."
            )
        board_qty_idx = header_parts.index(qty_col)
        src_rows = parse_board_table(folder)
        for r in src_rows:
            if len(r) < 12:
                continue
            refdes, spec, mpn, manuf, dk, mouser, jlc, alt, notes, footA, footD, qty = r[:12]
            row = ["-"] * n_cols
            row[boardrefdes_idx] = f"{code}: {refdes}"
            row[mpn_idx] = mpn
            row[dk_idx] = dk
            row[mouser_idx] = mouser
            row[jlc_idx] = jlc
            row[alt_idx] = alt
            row[board_qty_idx] = qty
            row[sysqty_idx] = qty
            combined_notes = spec
            if manuf and manuf != "-":
                combined_notes += f" [{manuf}]"
            if notes and notes not in ("-", ""):
                combined_notes += f"; {notes}"
            row[notes_idx] = combined_notes
            row[footA_idx] = footA
            row[footD_idx] = footD
            new_rows_md.append("| " + " | ".join(row) + " |\n")

    with open(BOM_PATH, "a", encoding="utf-8") as f:
        f.writelines(new_rows_md)

    print(f"Appended {len(new_rows_md)} new rows across {len(boards)} boards.")


if __name__ == "__main__":
    main()
