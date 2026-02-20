import pdfToMarkdown
import vectorDBBuilder
import chromadb
from chromadb.utils import embedding_functions
from time import sleep, time

def _wait_for_chroma():
    for _ in range(10):
        try:
            client = chromadb.HttpClient(host="chroma", port=8000)
            client.heartbeat()
            return client
        except Exception:
            print("⏳ Waiting for Chroma...")
            time.sleep(2)
    raise RuntimeError("Chroma not ready")

def init_db():
    _wait_for_chroma()
    pdfToMarkdown.main()
    vectorDBBuilder.main()
