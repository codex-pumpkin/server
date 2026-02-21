from src.persistence.impl.chroma_database.pdfToMarkdown import convert_pdf_to_markdown
from src.persistence.impl.chroma_database import vectorDBBuilder
import chromadb
from chromadb.utils import embedding_functions
from pathlib import Path
import time
import logging
import hashlib
import json
from colorama import init, Fore, Style

init(autoreset=True)
CACHE = Path("docs_cache.json")


def _wait_for_chroma():
    for _ in range(10):
        try:
            client = chromadb.HttpClient(host="chroma", port=8000)
            client.heartbeat()
            return client
        except Exception:
            logging.info(Fore.GREEN + "Waiting for Chroma...")
            time.sleep(2)
    logging.error(Fore.GREEN + "Chroma did not respond after multiple attempts.")
    raise RuntimeError(Fore.GREEN + "Chroma not ready")

def _check_if_chroma_is_empty(client, collection_name="SPICE_Docs"):
    try:
        collection = client.get_collection(name=collection_name)
        if collection.count() > 0:
            logging.info(Fore.GREEN + "ChromaDB already has data. Skipping initialization.")
            return False
    except Exception:
        # Collection does not exist, which is expected on first run
        pass
    return True    


def init_db():
    client =_wait_for_chroma()

    chroma_empty = _check_if_chroma_is_empty(client)
    source = Path("/app/docs")
    source.mkdir(exist_ok=True)

    current_hashes = _compute_current_hashes(source)
    if not chroma_empty:
        cached_hashes = _load_cache()
        if current_hashes != cached_hashes:
            logging.info(Fore.GREEN + "Document changes detected. Reinitializing ChromaDB...")
            client.delete_collection(name="SPICE_Docs")
        else:
            logging.info(Fore.GREEN + "No document changes detected. Skipping ChromaDB initialization.")
            return    
        
    output = Path("markdown")
    output.mkdir(exist_ok=True)
    
    logging.info(Fore.GREEN + "Converting PDFs to Markdown...")
    convert_pdf_to_markdown(
        source=source,
        output=output
    )
    logging.info(Fore.GREEN + "Vectorizing Markdown files and populating ChromaDB...")
    vectorDBBuilder.main(source=output)
    _save_cache(current_hashes)
    logging.info(Fore.GREEN + "ChromaDB initialization complete.")


def _file_hash(path: Path) -> str:
    hasher = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()


def _compute_current_hashes(source: Path) -> dict:
    return {
        pdf.name: [_file_hash(pdf), pdf.stat().st_size, pdf.stat().st_mtime]
        for pdf in source.glob("*.pdf")
    }


def _load_cache() -> dict:
    if CACHE.exists():
        return json.loads(CACHE.read_text())
    return {}


def _save_cache(cache: dict):
    CACHE.write_text(json.dumps(cache))

