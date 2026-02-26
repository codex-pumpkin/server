import logging
from pathlib import Path
import uuid
import tiktoken
import chromadb
from typing import Union
from chromadb.utils import embedding_functions

from src.core import settings

enc = tiktoken.get_encoding("cl100k_base")

collection_entries = []

''' Function to chunk text by tokens
    max_tokens: maximum tokens per chunk  
    overlap: number of overlapping tokens between chunks
    Returns a list of text chunks
'''
def chunk_by_tokens(text : str, max_tokens=500, overlap=100) -> list[str]:
    """Chunk by tokens."""
    tokens = enc.encode(text)
    chunks = []

    start = 0
    while start < len(tokens):
        end = start + max_tokens
        chunk = enc.decode(tokens[start:end])
        chunks.append(chunk)
        start = end - overlap

    return chunks

'''Read markdown files and create chunks
   For each chunk, create metadata and unique ID
   Store in documents, metadatas, and ids lists
'''
def main(source:Union[Path, str]) -> None:
    """Main."""
    for md_file in source.glob("*.md"):
        name = md_file.name
        content = md_file.read_text(encoding="utf-8")
        chunks = chunk_by_tokens(content)

        for i, chunk in enumerate(chunks):
            metadata = {
                "source": name,
                "chunk": i
            }

            collection_entry = (chunk, metadata, str(uuid.uuid4()))
            collection_entries.append(collection_entry)

    if len(collection_entries) == 0:
        logging.error("At minimum one PDF file that contains text needs to be present under /app/documents.")
        exit(1)

    build_vector_db()        


'''Initialize ChromaDB client and get or create collection
   Add documents to the collection
'''
def build_vector_db(source:Union[Path, str]="./chroma_db", namedb: str="SPICE_Docs") -> None:
    """Build vector db."""
    client = chromadb.HttpClient(host=settings.chroma_settings.host, port=settings.chroma_settings.port)

    collection = client.get_or_create_collection(
        name=namedb,
        embedding_function=embedding_functions.DefaultEmbeddingFunction()
    )

    docs = [entry[0] for entry in collection_entries]
    metadatas = [entry[1] for entry in collection_entries]
    ids = [entry[2] for entry in collection_entries]

    collection.add(
        documents=docs,
        metadatas=metadatas,
        ids=ids
    )

if __name__ == "__main__":
    folder = Path("markdown")
    main(folder)
