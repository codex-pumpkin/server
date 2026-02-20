from src.persistence.impl.chroma_database.pdfToMarkdown import convert_pdf_to_markdown
from src.persistence.impl.chroma_database import vectorDBBuilder
import chromadb
from chromadb.utils import embedding_functions
from pathlib import Path
from time import sleep, time
import logging

def _wait_for_chroma():
    for _ in range(10):
        try:
            client = chromadb.HttpClient(host="chroma", port=8000)
            client.heartbeat()
            return client
        except Exception:
            logging.info("⏳ Waiting for Chroma...")
            time.sleep(2)
    raise RuntimeError("Chroma not ready")

def init_db():
    _wait_for_chroma()
    
    source = Path("docs")
    source.mkdir(exist_ok=True)
    output = Path("markdown")
    output.mkdir(exist_ok=True)
    
    logging.info("Converting PDFs to Markdown...")
    convert_pdf_to_markdown(
        source=source,
        output=output
    )
    logging.info("Vectorizing Markdown files and populating ChromaDB...")
    vectorDBBuilder.main(source=output)
    logging.info("ChromaDB initialization complete.")
