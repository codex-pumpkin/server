import importlib
import io
import json
import types

import pytest
import tiktoken

from src.core import settings


class FakeEncoding:
    def encode(self, text):
        return text.split()

    def decode(self, tokens):
        return " ".join(tokens)


tiktoken.get_encoding = lambda name: FakeEncoding()

vector_module = importlib.import_module("src.persistence.impl.chroma_database.vectorDBBuilder")
pdf_module = importlib.import_module("src.persistence.impl.chroma_database.pdfToMarkdown")
init_module = importlib.import_module("src.persistence.impl.chroma_database.initDB")
semantic_module = importlib.import_module("src.persistence.impl.chroma_database.SemanticRepository")
SemanticRepository = semantic_module.SemanticRepository

def test_strip_page_markers_and_extract_spice_blocks():
    text = (
        "<!-- PAGE:2 | CHAPTER:Filters | SECTION:RC -->\n"
        "* title\nV1 1 0 DC 5\nR1 1 2 1k\nC1 2 0 1u\n.print tran v(2)\n.end\n"
    )

    clean, chapter, section = vector_module.strip_page_markers(text)
    blocks = vector_module.extract_spice_blocks(clean)

    assert chapter == "Filters"
    assert section == "RC"
    assert "<!--" not in clean
    assert len(blocks) == 1
    assert "V1 1 0 DC 5" in blocks[0]


def test_split_into_sections_chunking_toc_and_prefix(monkeypatch):
    monkeypatch.setattr(vector_module, "enc", FakeEncoding())

    sections = vector_module.split_into_sections("# Intro\nBody\n\n## Details\nMore")
    fallback = vector_module.split_into_sections("One paragraph\n\nTwo paragraph")
    chunks = vector_module.chunk_by_tokens("a b c d e", max_tokens=3, overlap=1)

    assert sections == [("Intro", "Body"), ("Details", "More")]
    assert fallback == [("", "One paragraph"), ("", "Two paragraph")]
    assert chunks == ["a b c", "c d e"]
    assert vector_module.is_toc_chunk("1 Intro ..... 10\n2 Body ..... 12\n3 End ..... 20") is True
    assert vector_module.is_toc_chunk("real content line\nanother content line\nthird line") is False
    assert vector_module._build_prefix("Filters", "RC", "manual") == "[manual | Chapter: Filters | Section: RC]\n"


def test_process_markdown_file_builds_spice_and_text_entries(monkeypatch):
    monkeypatch.setattr(vector_module, "enc", FakeEncoding())
    monkeypatch.setattr(vector_module, "chunk_by_tokens", lambda text, *args, **kwargs: [text + " extra tokens here"])

    md_file = types.SimpleNamespace(
        stem="manual",
        read_text=lambda encoding="utf-8": "\n".join(
            [
                "<!-- PAGE:1 | CHAPTER:Filters | SECTION:Intro -->",
                "# Intro",
                "This is a long explanation about rc filters and circuit design choices.",
                "* title",
                "V1 1 0 DC 5",
                "R1 1 2 1k",
                "C1 2 0 1u",
                ".print tran v(2)",
                ".end",
            ]
        ),
    )

    entries = vector_module.process_markdown_file(md_file)

    assert len(entries) == 1
    assert entries[0][1]["type"] == "spice_block"
    assert "[manual | Chapter: Filters | Section: Intro]" in entries[0][0]
    assert "This is a long explanation" in entries[0][0]


def test_build_vector_db_batches_documents(monkeypatch):
    vector_module.collection_entries[:] = [
        ("doc1", {"source": "a"}, "id1"),
        ("doc2", {"source": "a"}, "id2"),
        ("doc3", {"source": "b"}, "id3"),
    ]

    deleted = []
    added_batches = []

    class FakeCollection:
        def add(self, documents, metadatas, ids):
            added_batches.append((documents, metadatas, ids))

    class FakeClient:
        def delete_collection(self, name):
            deleted.append(name)

        def get_or_create_collection(self, **kwargs):
            self.kwargs = kwargs
            return FakeCollection()

    fake_client = FakeClient()
    monkeypatch.setattr(vector_module.chromadb, "HttpClient", lambda **kwargs: fake_client)
    monkeypatch.setattr(vector_module.embedding_functions, "DefaultEmbeddingFunction", lambda: "default-embedding")
    monkeypatch.setattr(settings.llm_settings, "api_key", "")

    vector_module.build_vector_db(batch_size=2)

    assert deleted == ["SPICE_Docs"]
    assert fake_client.kwargs["embedding_function"] == "default-embedding"
    assert len(added_batches) == 2
    assert added_batches[0][0] == ["doc1", "doc2"]
    assert added_batches[1][0] == ["doc3"]


def test_main_processes_markdown_and_exits_when_empty(monkeypatch):
    processed = []
    built = []
    vector_module.collection_entries[:] = []

    md_file = types.SimpleNamespace(stem="sample")
    fake_source = types.SimpleNamespace(glob=lambda pattern: [md_file])
    empty_source = types.SimpleNamespace(glob=lambda pattern: [])

    monkeypatch.setattr(vector_module, "Path", lambda source: fake_source)
    monkeypatch.setattr(vector_module, "process_markdown_file", lambda path: [("chunk", {"source": path.stem}, "id")])
    monkeypatch.setattr(vector_module, "build_vector_db", lambda: built.append(True))

    vector_module.main("ignored")

    assert built == [True]
    assert vector_module.collection_entries

    vector_module.collection_entries[:] = []
    monkeypatch.setattr(vector_module, "build_vector_db", lambda: processed.append(True))
    monkeypatch.setattr(vector_module, "Path", lambda source: empty_source)

    with pytest.raises(SystemExit):
        vector_module.main("missing")

    assert processed == []


def test_clean_ocr_text_extract_toc_and_convert_pdf(monkeypatch):
    cleaned = pdf_module.clean_ocr_text("word-\nwrap\n\n\n42\nabc  \t  def\n")
    assert "wordwrap" in cleaned
    assert "42" not in cleaned
    assert "\n\n\n" not in cleaned

    class FakeDoc:
        def __init__(self, toc=None, pages=0):
            self._toc = toc or []
            self._pages = pages
            self.closed = False

        def get_toc(self):
            return self._toc

        def close(self):
            self.closed = True

        def __len__(self):
            return self._pages

    page_doc = FakeDoc(pages=2)
    opened = [page_doc]

    monkeypatch.setattr(pdf_module.pymupdf, "open", lambda path: opened.pop(0))
    monkeypatch.setattr(pdf_module, "extract_toc", lambda pdf: [{"level": 1, "title": "Chapter", "page": 1}, {"level": 2, "title": "Section", "page": 2}])
    monkeypatch.setattr(
        pdf_module.pymupdf4llm,
        "to_markdown",
        lambda path, pages: " Page content " if pages == [0] else "",
    )

    written = {}

    class FakeOutputFile:
        def __init__(self, name):
            self.name = name

        def write_text(self, content, encoding="utf-8"):
            written[self.name] = content

    class FakeOutputDir:
        def mkdir(self, parents=False, exist_ok=False):
            return None

        def __truediv__(self, name):
            return FakeOutputFile(name)

    fake_pdf = types.SimpleNamespace(stem="manual")
    fake_source = types.SimpleNamespace(glob=lambda pattern: [fake_pdf])

    monkeypatch.setattr(pdf_module, "Path", lambda value: fake_source if value == "source" else FakeOutputDir())

    pdf_module.convert_pdf_to_markdown("source", "output")
    content = written["manual.md"]

    assert "PAGE:1" in content
    assert "CHAPTER:Chapter" in content
    assert "Page content" in content
    assert pdf_module.get_section_for_page(1, [{"level": 1, "title": "Chapter", "page": 1}, {"level": 2, "title": "Section", "page": 2}]) == ("Chapter", "Section")


def test_init_db_helpers_and_semantic_repository(monkeypatch):
    cache_state = {"exists": False, "text": ""}

    class FakeCache:
        def exists(self):
            return cache_state["exists"]

        def read_text(self):
            return cache_state["text"]

        def write_text(self, text):
            cache_state["exists"] = True
            cache_state["text"] = text

    pdf_file = types.SimpleNamespace(
        name="doc.pdf",
        stat=lambda: types.SimpleNamespace(st_size=3, st_mtime=10.0),
    )
    source = types.SimpleNamespace(glob=lambda pattern: [pdf_file])

    monkeypatch.setattr("builtins.open", lambda path, mode="rb": io.BytesIO(b"pdf"))
    assert init_module._file_hash(object())

    monkeypatch.setattr(init_module, "CACHE", FakeCache())
    monkeypatch.setattr(init_module, "_file_hash", lambda path: "hash")

    hashes = init_module._compute_current_hashes(source)
    assert hashes == {"doc.pdf": ["hash", 3, 10.0]}
    assert init_module._load_cache() == {}

    init_module._save_cache({"a": 1})
    assert json.loads(cache_state["text"]) == {"a": 1}
    assert init_module._load_cache() == {"a": 1}

    attempts = {"count": 0}

    class HeartbeatClient:
        def heartbeat(self):
            attempts["count"] += 1
            if attempts["count"] < 3:
                raise RuntimeError("not ready")

    monkeypatch.setattr(init_module.chromadb, "HttpClient", lambda **kwargs: HeartbeatClient())
    monkeypatch.setattr(init_module.time, "sleep", lambda seconds: None)
    client = init_module._wait_for_chroma()
    assert attempts["count"] == 3
    assert isinstance(client, HeartbeatClient)

    class EmptyCollection:
        def __init__(self, count):
            self._count = count

        def count(self):
            return self._count

    class CollectionClient:
        def __init__(self, count=None):
            self._count = count

        def get_collection(self, name):
            if self._count is None:
                raise RuntimeError("missing")
            return EmptyCollection(self._count)

    assert init_module._check_if_chroma_is_empty(CollectionClient(0)) is True
    assert init_module._check_if_chroma_is_empty(CollectionClient(2)) is False
    assert init_module._check_if_chroma_is_empty(CollectionClient(None)) is True

    semantic_module._chroma_client = None

    class SimilarCollection:
        def query(self, **kwargs):
            return {"documents": [["chunk-1", "chunk-2"]]}

    class SemanticClient:
        def get_collection(self, **kwargs):
            return SimilarCollection()

    monkeypatch.setattr(semantic_module.SemanticRepository, "_chromadb", staticmethod(lambda: types.SimpleNamespace(HttpClient=lambda **kwargs: SemanticClient())))
    monkeypatch.setattr(
        semantic_module,
        "embedding_functions",
        types.SimpleNamespace(DefaultEmbeddingFunction=lambda: "embed", OpenAIEmbeddingFunction=lambda **kwargs: "openai"),
        raising=False,
    )
    monkeypatch.setattr(settings.llm_settings, "api_key", "")

    repo = SemanticRepository(connect=True)
    assert repo.collection is not None


@pytest.mark.asyncio
async def test_init_db_flow_and_semantic_query(monkeypatch):
    source = types.SimpleNamespace(mkdir=lambda exist_ok=False: None)
    output = types.SimpleNamespace(mkdir=lambda exist_ok=False: None)

    monkeypatch.setattr(init_module, "Path", lambda value: source if value == "/app/documents" else output)

    delete_calls = []
    converted = []
    vectorized = []
    saved = []

    class InitClient:
        def __init__(self, empty):
            self.empty = empty

        def delete_collection(self, name):
            delete_calls.append(name)

    monkeypatch.setattr(init_module, "_wait_for_chroma", lambda: InitClient(empty=False))
    monkeypatch.setattr(init_module, "_check_if_chroma_is_empty", lambda client: False)
    monkeypatch.setattr(init_module, "_compute_current_hashes", lambda src: {"manual.pdf": ["hash", 4, 1.0]})
    monkeypatch.setattr(init_module, "_load_cache", lambda: {"manual.pdf": ["old", 4, 1.0]})
    monkeypatch.setattr(init_module, "_save_cache", lambda cache: saved.append(cache))
    monkeypatch.setattr(init_module, "convert_pdf_to_markdown", lambda source, output: converted.append((source, output)))
    monkeypatch.setattr(init_module.vectorDBBuilder, "main", lambda source: vectorized.append(source))

    init_module.init_db()

    assert delete_calls == ["SPICE_Docs"]
    assert converted == [(source, output)]
    assert vectorized == [output]
    assert saved == [{"manual.pdf": ["hash", 4, 1.0]}]

    semantic_module._chroma_client = None

    class SimilarCollection:
        def query(self, **kwargs):
            return {"documents": [["chunk-a", "chunk-b"]]}

    class SemanticClient:
        def get_collection(self, **kwargs):
            return SimilarCollection()

    monkeypatch.setattr(semantic_module.SemanticRepository, "_chromadb", staticmethod(lambda: types.SimpleNamespace(HttpClient=lambda **kwargs: SemanticClient())))
    monkeypatch.setattr(
        semantic_module,
        "embedding_functions",
        types.SimpleNamespace(DefaultEmbeddingFunction=lambda: "embed", OpenAIEmbeddingFunction=lambda **kwargs: "openai"),
        raising=False,
    )
    monkeypatch.setattr(settings.llm_settings, "api_key", "")

    repo = SemanticRepository(connect=True)
    empty_repo = SemanticRepository(connect=False)

    assert await repo.get_similar_chunks("oscillator", 2) == ["chunk-a", "chunk-b"]
    assert await empty_repo.get_similar_chunks("oscillator", 2) == []
