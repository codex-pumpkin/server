import pymupdf4llm
import pymupdf
import re
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
    toc = doc.get_toc()  # [[level, title, page], ...]
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

    for pdf_file in source.glob("*.pdf"):
        name = pdf_file.stem
        md_path = output / f"{name}.md"

        toc = extract_toc(pdf_file)
        doc = pymupdf.open(str(pdf_file))
        parts = []

        for page_num in range(len(doc)):
            page_md = pymupdf4llm.to_markdown(str(pdf_file), pages=[page_num])
            page_md = clean_ocr_text(page_md)

            if not page_md.strip():
                continue

            chapter, section = get_section_for_page(page_num, toc)

            # Metadata marker — used by vectorDBBuilder for heading-prefixed chunks
            marker = (
                f"\n<!-- PAGE:{page_num + 1} | "
                f"CHAPTER:{chapter} | "
                f"SECTION:{section} -->\n"
            )
            parts.append(marker + page_md)

        doc.close()

        full_md = "\n".join(parts)
        md_path.write_text(full_md, encoding="utf-8")


def main() -> None:
    folder = Path("/app/docs")
    output_folder = Path("markdown")
    convert_pdf_to_markdown(folder, output_folder)


if __name__ == "__main__":
    main()