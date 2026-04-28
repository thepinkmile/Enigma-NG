from __future__ import annotations

import json
import re
import sys
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import pdfplumber
from pypdf import PdfReader


ROOT = Path(r"C:\_DATA_\Repositories\github\Enigma-NG")
DATASHEETS_DIR = ROOT / "design" / "Datasheets"
INVENTORY_PATH = DATASHEETS_DIR / "_generated_markdown_inventory.json"

MANUAL_PDF_TO_MD_MAP = {
    "Glenair_03232018_807_216-3045547-datasheet.pdf": "Glenair-807-216-datasheet.md",
    "Glenair_mighty-mouse-807-nw-connector_catalogue.pdf": "Glenair-807-216-datasheet.md",
}


BOILERPLATE_PATTERNS = [
    re.compile(r"^\s*$"),
    re.compile(r"^\d+\s*$"),
    re.compile(r"^[A-Z0-9-]+(?:\s+[A-Z0-9-]+)?\s+\d+$"),
    re.compile(r"^(features|applications|description|table of contents)$", re.I),
    re.compile(r"^an important notice", re.I),
    re.compile(r"^datasheet", re.I),
    re.compile(r"^preliminary", re.I),
    re.compile(r"^production data", re.I),
]


SECTION_KEYWORDS = {
    "Part number and ordering information": [
        "part number",
        "ordering",
        "orderable",
        "device information",
        "package information",
        "nomenclature",
        "suffix",
        "option",
        "marking",
    ],
    "Pin, pad, and connection designations": [
        "pin",
        "pin functions",
        "pin configuration",
        "terminal",
        "pad",
        "connection",
        "signal",
        "ball",
        "port",
    ],
    "Specifications, ratings, and operating conditions": [
        "absolute maximum",
        "recommended operating",
        "electrical characteristics",
        "thermal",
        "recommended conditions",
        "dc characteristics",
        "ac characteristics",
        "timing",
        "ratings",
        "specification",
        "tolerance",
        "current",
        "voltage",
    ],
    "Dimensions, package, and mechanical information": [
        "dimension",
        "package",
        "outline",
        "land pattern",
        "footprint",
        "mechanical",
        "drawing",
        "recommended pcb",
        "recommended pad",
        "body size",
    ],
    "Formulas, equations, and configurable calculations": [
        "equation",
        "formula",
        "where:",
        "calculate",
        "computed",
        "set by",
        "determined by",
        "ratio",
        "gain",
        "ilimit",
        "ilim",
        "uvlo",
        "dvdt",
    ],
    "Reference designs, applications, and examples": [
        "application",
        "reference design",
        "example",
        "typical application",
        "simplified schematic",
        "implementation",
        "layout example",
        "evaluation",
    ],
}


@dataclass
class PageExtraction:
    page_number: int
    text: str


def normalize_text(text: str) -> str:
    text = text.replace("\x00", " ").replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


_BARE_URL_RE = re.compile(
    r"(?<![(<`\"])"
    r"((?:https?://|www\.)\S+|[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,})"
)


def escape_snippet(text: str, max_len: int = 195) -> str:
    """Escape raw PDF snippet text for safe rendering as a markdown bullet."""
    text = text.replace("\\", "\\\\")
    text = text.replace("*", "\\*")
    text = text.replace("_", "\\_")
    text = _BARE_URL_RE.sub(r"<\1>", text)
    if len(text) > max_len:
        text = text[:max_len - 1] + "…"
    return text


def wrap_text_block(text: str, width: int = 100) -> str:
    if not text.strip():
        return ""

    paragraphs = []
    for block in re.split(r"\n\s*\n", text.strip()):
        lines = []
        for raw_line in block.splitlines():
            line = raw_line.strip()
            if not line:
                continue
            wrapped = textwrap.fill(
                line,
                width=width,
                break_long_words=False,
                break_on_hyphens=False,
            )
            lines.append(wrapped)
        if lines:
            paragraphs.append("\n".join(lines))
    return "\n\n".join(paragraphs)


def extract_page_text(pdf_path: Path) -> list[PageExtraction]:
    reader = PdfReader(str(pdf_path))
    pages: list[PageExtraction] = []

    with pdfplumber.open(str(pdf_path)) as plumber_pdf:
        for index, page in enumerate(reader.pages, start=1):
            pypdf_text = normalize_text(page.extract_text() or "")
            if len(pypdf_text) < 80:
                plumber_text = normalize_text(plumber_pdf.pages[index - 1].extract_text() or "")
                text = plumber_text if len(plumber_text) > len(pypdf_text) else pypdf_text
            else:
                text = pypdf_text
            pages.append(PageExtraction(page_number=index, text=text))

    return pages


def pick_title(pages: list[PageExtraction], fallback: str) -> str:
    if not pages:
        return fallback

    first_lines = []
    for page in pages[:2]:
        first_lines.extend(page.text.splitlines()[:40])

    cleaned: list[str] = []
    for line in first_lines:
        candidate = re.sub(r"\s+", " ", line).strip(" -\t")
        if len(candidate) < 6:
            continue
        if any(pattern.match(candidate) for pattern in BOILERPLATE_PATTERNS):
            continue
        cleaned.append(candidate)

    TRAILING_PUNCT = set(".,;:!?")
    _CONTACT_RE = re.compile(r"www\.|fax:|tel:|phone:|@|\d{3}[\-.\s]\d{3,}", re.I)
    for candidate in cleaned:
        if ":" in candidate and not _CONTACT_RE.search(candidate):
            return candidate.rstrip("".join(TRAILING_PUNCT))
    for candidate in cleaned:
        if not _CONTACT_RE.search(candidate):
            result = candidate
            break
    else:
        result = cleaned[0] if cleaned else fallback
    return result.rstrip("".join(TRAILING_PUNCT))


def find_snippets(lines: Iterable[str], keywords: list[str], window: int = 2, limit: int = 20) -> list[str]:
    source_lines = list(lines)
    snippets: list[str] = []
    seen = set()
    lowered_keywords = [keyword.lower() for keyword in keywords]

    for index, line in enumerate(source_lines):
        line_l = line.lower()
        if not any(keyword in line_l for keyword in lowered_keywords):
            continue

        start = max(0, index - window)
        end = min(len(source_lines), index + window + 1)
        snippet = "\n".join(l.strip() for l in source_lines[start:end] if l.strip())
        snippet = normalize_text(snippet)
        if not snippet:
            continue
        key = re.sub(r"\s+", " ", snippet.lower())
        if key in seen:
            continue
        seen.add(key)
        snippets.append(snippet)
        if len(snippets) >= limit:
            break

    return snippets


def build_markdown(pdf_path: Path) -> str:
    pages = extract_page_text(pdf_path)
    reader = PdfReader(str(pdf_path))
    metadata = reader.metadata or {}
    title = pick_title(pages, pdf_path.stem)
    combined_lines = []
    for page in pages:
        combined_lines.extend(page.text.splitlines())

    md_lines: list[str] = []
    md_lines.append(f"# {title}")
    md_lines.append("")
    md_lines.append("## Source")
    md_lines.append("")
    md_lines.append(f"- **Source PDF:** [{pdf_path.name}]({pdf_path.name})")
    md_lines.append(f"- **Generated Markdown:** `{pdf_path.stem}.md`")
    md_lines.append(f"- **Page count:** {len(pages)}")
    md_lines.append("- **Conversion method:** automated local PDF text extraction with pypdf/pdfplumber")
    md_lines.append("")

    md_lines.append("## PDF Metadata")
    md_lines.append("")
    md_lines.append("| Field | Value |")
    md_lines.append("| :--- | :--- |")
    for key in ("title", "author", "subject", "creator", "producer"):
        value = getattr(metadata, key, None) if hasattr(metadata, key) else metadata.get(f"/{key.title()}")
        escaped_value = str(value or "").replace("|", "\\|")
        md_lines.append(f"| {key.title()} | {escaped_value} |")
    md_lines.append("")

    md_lines.append("## Extracted Technical Index")
    md_lines.append("")
    md_lines.append(
        "This markdown datasheet is meant to reduce the need to reopen the PDF during design work."
    )
    md_lines.append(
        "It preserves design-relevant extracted snippets first, followed by page-by-page text "
        "so the source content remains locally searchable."
    )
    md_lines.append("")

    for section_title, keywords in SECTION_KEYWORDS.items():
        snippets = find_snippets(combined_lines, keywords)
        md_lines.append(f"### {section_title}")
        md_lines.append("")
        if snippets:
            for snippet in snippets:
                escaped = escape_snippet(snippet.replace(chr(10), ' / '))
                md_lines.append(f"- {escaped}")
        else:
            md_lines.append("- No reliable text snippet was automatically extracted for this category. Review the raw page text below.")
        md_lines.append("")

    md_lines.append("## Page-by-Page Extracted Content")
    md_lines.append("")
    for page in pages:
        md_lines.append(f"### Page {page.page_number}")
        md_lines.append("")
        if page.text.strip():
            md_lines.append("```text")
            md_lines.append(page.text)
            md_lines.append("```")
        else:
            md_lines.append("_No text could be extracted from this page with the current local extractor._")
        md_lines.append("")

    return "\n".join(md_lines).rstrip() + "\n"


def build_inventory() -> dict[str, object]:
    pdf_files = sorted(path.name for path in DATASHEETS_DIR.glob("*.pdf"))
    markdown_files = sorted(
        path.name
        for path in DATASHEETS_DIR.glob("*.md")
        if path.name != INVENTORY_PATH.name
    )
    markdown_set = set(markdown_files)

    mappings = []
    pdf_only = []

    for pdf_name in pdf_files:
        markdown_name = MANUAL_PDF_TO_MD_MAP.get(pdf_name, f"{Path(pdf_name).stem}.md")
        if markdown_name in markdown_set:
            mapping_type = "manual" if pdf_name in MANUAL_PDF_TO_MD_MAP else "same_stem"
            mappings.append(
                {
                    "pdf": pdf_name,
                    "markdown": markdown_name,
                    "mapping_type": mapping_type,
                }
            )
        else:
            pdf_only.append(pdf_name)

    mapped_markdowns = {entry["markdown"] for entry in mappings}
    markdown_only = sorted(name for name in markdown_files if name not in mapped_markdowns)

    return {
        "maintained_by": r".copilot\agent-scripts\generate_markdown_datasheets.py",
        "lookup_order": [
            "markdown datasheet",
            "local PDF datasheet",
            "online source only if local sources are missing or insufficient",
        ],
        "pdf_to_markdown": mappings,
        "pdf_only": pdf_only,
        "markdown_only": markdown_only,
    }


def main() -> None:
    if len(sys.argv) > 1:
        pdf_files = [Path(arg) for arg in sys.argv[1:]]
    else:
        pdf_files = sorted(DATASHEETS_DIR.glob("*.pdf"))

    generated = []
    for pdf_path in pdf_files:
        md_path = pdf_path.with_suffix(".md")
        markdown = build_markdown(pdf_path)
        md_path.write_text(markdown, encoding="utf-8", newline="\n")
        generated.append({"pdf": pdf_path.name, "markdown": md_path.name})

    inventory = build_inventory()
    INVENTORY_PATH.write_text(json.dumps(inventory, indent=2), encoding="utf-8", newline="\n")
    print(
        f"Generated {len(generated)} markdown datasheet(s) and rebuilt {INVENTORY_PATH.name}."
    )


if __name__ == "__main__":
    main()
