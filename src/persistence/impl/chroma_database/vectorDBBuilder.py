import re
import uuid
from pathlib import Path
from typing import Union
 
import tiktoken
import chromadb
from chromadb.utils import embedding_functions
 
from src.core import settings
 
CHUNK_MAX_TOKENS = 400
CHUNK_OVERLAP_TOKENS = 80
 
enc = tiktoken.get_encoding("cl100k_base")
 
collection_entries: list[tuple[str, dict, str]] = []
 
PAGE_MARKER_RE = re.compile(
    r'<!--\s*PAGE:(\d+)\s*\|\s*CHAPTER:([^|]+?)\s*\|\s*SECTION:([^-]*?)\s*-->'
)
 
 
def strip_page_markers(text: str) -> tuple[str, str, str]:
    """
    Remove page markers and return (clean_text, chapter, section).
    Returns empty strings for chapter/section if no markers found.
    """
    chapter, section = "", ""
    for match in PAGE_MARKER_RE.finditer(text):
        chapter = match.group(2).strip()
        section = match.group(3).strip()
    clean = PAGE_MARKER_RE.sub("", text).strip()
    return clean, chapter, section


SPICE_BLOCK_RE = re.compile(
    r'(?:^[ \t]*(?:\*[^\n]*|\.subckt\b[^\n]*|\.ends\b[^\n]*|\.model\b[^\n]*'
    r'|\.tran\b[^\n]*|\.ac\b[^\n]*|\.dc\b[^\n]*|\.print\b[^\n]*|\.plot\b[^\n]*'
    r'|\.end\b[^\n]*|\.ic\b[^\n]*|\.param\b[^\n]*'
    r'|[VIRCLEBFGHTQDMJKZXOUvirlcebfghtqdmjkzxou]\w*\s+\S+[^\n]*)\n){3,}',  
    re.MULTILINE
)
 
 
def extract_spice_blocks(text: str) -> list[str]:
    """Extract SPICE netlist blocks as atomic strings."""
    return [m.group(0).strip() for m in SPICE_BLOCK_RE.finditer(text) if m.group(0).strip()]

 
def split_into_sections(text: str) -> list[tuple[str, str]]:
    """
    Split markdown text at heading boundaries.
    Returns list of (heading, body) tuples.
    Falls back to paragraph splitting if no headings found.
    """
    # Split on lines that start with # (markdown headings)
    parts = re.split(r'\n(?=#{1,4} )', text)
 
    if len(parts) <= 1:
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        return [("", p) for p in paragraphs]
 
    result = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        heading_match = re.match(r'^(#{1,4} .+)', part)
        if heading_match:
            heading = heading_match.group(1).replace('#', '').strip()
            body = part[heading_match.end():].strip()
            result.append((heading, body))
        else:
            result.append(("", part))
 
    return result
 
def chunk_by_tokens(text: str, max_tokens: int = CHUNK_MAX_TOKENS,
                    overlap: int = CHUNK_OVERLAP_TOKENS) -> list[str]:
    """Sliding window token chunker."""
    tokens = enc.encode(text)
    if not tokens:
        return []
    chunks = []
    start = 0
    while start < len(tokens):
        end = min(start + max_tokens, len(tokens))
        chunks.append(enc.decode(tokens[start:end]))
        if end == len(tokens):
            break
        start = end - overlap
    return chunks


 
def process_markdown_file(md_path: Path) -> list[tuple[str, dict, str]]:
    """
    Process one markdown file into enriched (text, metadata, id) entries.
 
    Each chunk text is prefixed with its section context:
        [Chapter: X | Section: Y]\n<chunk text>
 
    This prefix is the key improvement for semantic search — the embedding
    model sees the topic context even for short chunks, so similarity search
    finds Wien bridge chunks for Wien bridge queries instead of generic text.
    """
    content = md_path.read_text(encoding="utf-8")
    source_name = md_path.stem
    entries = []
    spice_block_texts = set()
 
    for block in extract_spice_blocks(content):
        spice_block_texts.add(block)
        pos = content.find(block)
        surrounding = content[max(0, pos - 500):pos]
        _, chapter, section = strip_page_markers(surrounding)
 
        prefix = _build_prefix(chapter, section, source_name)
        full_text = f"{prefix}{block}"
 
        entries.append((
            full_text,
            {"source": source_name, "chunk": len(entries), "type": "spice_block"},
            str(uuid.uuid4())
        ))
 
    text_without_spice = content
    for block in spice_block_texts:
        text_without_spice = text_without_spice.replace(block, "")
 
    _, doc_chapter, doc_section = strip_page_markers(text_without_spice)
    clean_text, _, _ = strip_page_markers(text_without_spice)

    sections = split_into_sections(clean_text)
 
    for heading, body in sections:
        if not body.strip():
            continue
        effective_section = heading or doc_section
 
        prefix = _build_prefix(doc_chapter, effective_section, source_name)
        prefixed_body = f"{prefix}{body}"
 
        # Chunk the prefixed text
        sub_chunks = chunk_by_tokens(prefixed_body)
 
        for i, chunk in enumerate(sub_chunks):
            if not chunk.strip():
                continue
            if is_toc_chunk(chunk):
                continue
            if len(enc.encode(chunk)) < 30:  # skip chunks under 30 tokens
                continue
            entries.append((
                chunk,
                {"source": source_name, "chunk": len(entries)},
                str(uuid.uuid4())
            ))

    return entries

def is_toc_chunk(text: str) -> bool:
    """
    Detect table of contents pages — dense dot-leaders and page numbers,
    no real content worth indexing.
    """
    lines = text.strip().splitlines()
    if len(lines) < 3:
        return False

    # TOC lines look like: "8.3.9 Some Title . . . . . . . 243"
    dot_leader_lines = sum(
        1 for line in lines
        if re.search(r'\.{3,}\s*\d+\s*$', line)
    )

    # If more than 40% of lines are TOC entries, skip this chunk
    return (dot_leader_lines / len(lines)) > 0.4
 
 
def _build_prefix(chapter: str, section: str, source: str) -> str:
    """
    Build a context prefix for a chunk.
    Example: "[ngspice-40-manual | Chapter: Oscillators | Section: Wien Bridge]\n"
 
    This prefix anchors the embedding to the topic even for short chunks.
    """
    parts = [source]
    if chapter:
        parts.append(f"Chapter: {chapter}")
    if section:
        parts.append(f"Section: {section}")
    return f"[{' | '.join(parts)}]\n"

 
def main(source: Union[Path, str]) -> None:
    """Read markdown files, chunk them, and store in ChromaDB."""
    source = Path(source)
 
    for md_file in source.glob("*.md"):
        file_entries = process_markdown_file(md_file)
        collection_entries.extend(file_entries)
 
    if not collection_entries:
        exit(1)
    build_vector_db()
 
 
def build_vector_db(
    namedb: str = "SPICE_Docs",
    batch_size: int = 100,
) -> None:
    """Insert chunks into ChromaDB. Same signature style as original."""
    client = chromadb.HttpClient(
        host=settings.chroma_settings.host,
        port=settings.chroma_settings.port
    )

    try:
        client.delete_collection(namedb)
    except Exception:
        pass
 
    collection = client.get_or_create_collection(
        name=namedb,
        embedding_function=embedding_functions.OpenAIEmbeddingFunction(
            api_key=settings.llm_settings.api_key,
            model_name="text-embedding-3-small"
        ),
        metadata={"hnsw:space": "cosine"},  
    )
 
    docs = [e[0] for e in collection_entries]
    metadatas = [e[1] for e in collection_entries]
    ids = [e[2] for e in collection_entries]
 
    for i in range(0, len(collection_entries), batch_size):
        batch_docs = docs[i:i + batch_size]
        batch_meta = metadatas[i:i + batch_size]
        batch_ids = ids[i:i + batch_size]
        collection.add(documents=batch_docs, metadatas=batch_meta, ids=batch_ids)
 
 
if __name__ == "__main__":
    folder = Path("markdown")
    main(folder)