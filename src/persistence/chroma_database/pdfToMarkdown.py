import pymupdf4llm
from pathlib import Path
from typing import Union

def convert_pdf_to_markdown(source:Union[Path, str], output:Union[Path, str]) -> None:
    source = Path(source)
    output = Path(output)
    for pdf_file in source.glob("*.pdf"):
        name = pdf_file.stem
        md_path = Path(output) / f"{name}.md"
        markdown = pymupdf4llm.to_markdown(pdf_file)
        md_path.write_text(markdown, encoding="utf-8")


def main() -> None:
    folder = Path("docs")
    output_folder = Path("markdown")
    convert_pdf_to_markdown(folder, output_folder)

if __name__ == "__main__":
    main()