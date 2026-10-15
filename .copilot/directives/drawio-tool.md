# Draw.io Tool Usage

- **Desktop app location:** `C:\Program Files\draw.io\draw.io.exe`. It is **not** on the system
  `PATH` - `where.exe drawio` / `Get-Command drawio` will incorrectly report it as missing. Always
  invoke it by its full path.
- **Rendering diagrams to PNG (project convention: PNG only, no SVG):**

  ```powershell
  & "C:\Program Files\draw.io\draw.io.exe" -x -f png -p <page-number> -o "<output.png>" "<input.drawio>"
  ```

  - `-p <page-number>` is 1-based; omit it only for single-page files (defaults to page 1).
  - Render every page of a multi-page `.drawio` file separately, once per page, to its own
    named PNG - do not rely on the default single-page export for multi-page files.
  - Harmless `ERROR:net\disk_cache\...`/`Gpu Cache Creation failed` lines on stderr do not
    indicate failure; check the output file was written instead.
- **File locations:** permanent `.drawio` sources live in `design/Diagrams/`; rendered PNGs live
  in `design/Diagrams/renders/`. Discussion-only/draft diagrams live under
  `.copilot/discussions/<topic>/` until promoted into `design/Diagrams/` per user instruction.
- **Workflow when editing a `.drawio` file:** after any edit, re-export and view the resulting
  PNG with the `view` tool to visually verify the change before reporting it as done - do not
  assume an XML-level edit rendered correctly without checking.
- **Multi-page files:** each `<diagram>` page has its own independent mxCell id namespace: the
  same id (e.g. `cypher`, `in-cypher`) can legitimately repeat across pages. A text edit targeting
  one page's cell will not automatically apply to another page's cell of the same id if their
  surrounding XML (e.g. `style` attributes) differs - verify both/all pages after a multi-page
  edit, not just the one you directly edited.
