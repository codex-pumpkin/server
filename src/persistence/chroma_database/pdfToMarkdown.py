import pymupdf4llm
from pathlib import Path


folder = Path("docs")
output_folder = Path("markdown")

for pdf_file in folder.glob("*.pdf"):
    name = pdf_file.stem
    md_path = Path(output_folder) / f"{name}.md"
    markdown = pymupdf4llm.to_markdown(pdf_file)
    md_path.write_text(markdown, encoding="utf-8")