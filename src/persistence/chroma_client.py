import chromadb
from chromadb.config import Settings

_chroma_client: chromadb.Client | None = None

# Get a singleton ChromaDB client instance
def get_chroma_client() -> chromadb.Client:
    global _chroma_client
    if _chroma_client is None:
        _chroma_client = chromadb.Client(
            Settings(
                persist_directory="/chroma_database/chroma_db",
                anonymized_telemetry=False,
            )
        )
    return _chroma_client