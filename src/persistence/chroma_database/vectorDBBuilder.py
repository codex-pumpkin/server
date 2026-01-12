from pathlib import Path
import uuid
import tiktoken
import chromadb
from chromadb.utils import embedding_functions

enc = tiktoken.get_encoding("cl100k_base")
folder = Path("markdown")

documents = []
metadatas = []
ids = []

# Function to chunk text by tokens
# max_tokens: maximum tokens per chunk
# overlap: number of overlapping tokens between chunks
# Returns a list of text chunks
def chunk_by_tokens(text, max_tokens=500, overlap=100):
    tokens = enc.encode(text)
    chunks = []

    start = 0
    while start < len(tokens):
        end = start + max_tokens
        chunk = enc.decode(tokens[start:end])
        chunks.append(chunk)
        start = end - overlap

    return chunks

# Read markdown files and create chunks
# For each chunk, create metadata and unique ID
# Store in documents, metadatas, and ids lists
for md_file in folder.glob("*.md"):
    name = md_file.name
    content = md_file.read_text(encoding="utf-8")
    chunks = chunk_by_tokens(content)

    for i, chunk in enumerate(chunks):
        documents.append(chunk)
        metadatas.append({
            "source": name,
            "chunk": i
        })
        ids.append(str(uuid.uuid4()))


# Initialize ChromaDB client and get or create collection
# Add documents to the collection
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="pdf_markdown",
    embedding_function=embedding_functions.DefaultEmbeddingFunction()
)

collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)
