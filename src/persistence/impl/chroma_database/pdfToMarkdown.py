import opendataloader_pdf
import pymupdf
import re
import tempfile
from pathlib import Path
from typing import Union


def clean_ocr_text(text: str) -> str:
    """
    Clean common OCR artifacts from PDF-extracted text.
    Targets issues seen in SPICE manuals (garbled chars, broken lines, etc.)
    """
    # Remove garbled unicode control characters
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', text)

    # Remove garbled OCR artifacts like ^j^™^™* seen in SPICE manual extraction
    text = re.sub(r'\^[a-zA-Z]\^[™®©°^]+\*?', '', text)
    text = re.sub(r'[™®©]{2,}', '', text)

    # Fix broken hyphenated words across lines (e.g. "tran-\nsient" -> "transient")
    text = re.sub(r'(\w)-\n(\w)', r'\1\2', text)

    # Remove lone page numbers (lines that are just a number)
    text = re.sub(r'^\s*\d+\s*$', '', text, flags=re.MULTILINE)

    # Collapse excessive blank lines (more than 2 -> 2)
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Normalize whitespace within lines
    text = re.sub(r'[ \t]{2,}', ' ', text)

    return text.strip()


def extract_toc(pdf_path: Path) -> list[dict]:
    """Extract table of contents entries from PDF."""
    doc = pymupdf.open(str(pdf_path))
    toc = doc.get_toc()
    doc.close()
    return [{"level": lvl, "title": title, "page": pg} for lvl, title, pg in toc]


def get_section_for_page(page_num: int, toc: list[dict]) -> tuple[str, str]:
    """Return (chapter, section) for a given 0-indexed page number."""
    chapter, section = "Introduction", ""
    for entry in toc:
        if entry["page"] <= page_num + 1:
            if entry["level"] == 1:
                chapter = entry["title"]
                section = ""
            elif entry["level"] == 2:
                section = entry["title"]
        else:
            break
    return chapter, section


def convert_pdf_to_markdown(source: Union[Path, str], output: Union[Path, str]) -> None:
    """
    Convert PDF files to cleaned markdown.

    Improvements over original:
    - Cleans OCR artifacts before saving
    - Inserts <!-- PAGE:N | CHAPTER:X | SECTION:Y --> markers per page
      so vectorDBBuilder can use them for context-aware chunking
    - Page-by-page extraction preserves section boundaries
    """
    source = Path(source)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)

    pdf_files = list(source.glob("*.pdf"))
    if not pdf_files:
        return

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)

        opendataloader_pdf.convert(
            input_path=[str(f) for f in pdf_files],
            output_dir=str(tmp_path),
            format="markdown",
        )

        for pdf_file in pdf_files:
            name = pdf_file.stem
            md_path = output / f"{name}.md"
            raw_md_path = tmp_path / f"{name}.md"

            if not raw_md_path.exists():
                continue

            raw_markdown = raw_md_path.read_text(encoding="utf-8")
            toc = extract_toc(pdf_file)

            page_separator = re.compile(r'\f|(?:^---\s*$)', re.MULTILINE)
            pages = page_separator.split(raw_markdown)

            parts = []
            for page_num, page_content in enumerate(pages):
                page_content = clean_ocr_text(page_content)

                if not page_content.strip():
                    continue

                chapter, section = get_section_for_page(page_num, toc)

                marker = (
                    f"\n<!-- PAGE:{page_num + 1} | "
                    f"CHAPTER:{chapter} | "
                    f"SECTION:{section} -->\n"
                )
                parts.append(marker + page_content)

            full_md = "\n".join(parts)
            md_path.write_text(full_md, encoding="utf-8")


def main() -> None:
    folder = Path("/app/docs")
    output_folder = Path("markdown")
    convert_pdf_to_markdown(folder, output_folder)


if __name__ == "__main__":
    main()