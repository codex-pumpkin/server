import asyncio
from typing import Any

from src.core import settings
from src.persistence.interfaces import ISemanticRepository

_chroma_client: Any | None = None


class SemanticRepository(ISemanticRepository):

    def __init__(self, namedb: str = "SPICE_Docs", connect: bool = True) -> None:
        """Initialize the semantic repository."""
        self.collection = None
        if connect:
            chromadb = self._chromadb()
            embedding_functions = self._embedding_functions()
            self.collection = self.get_chroma_client().get_collection(
                name=namedb,
<<<<<<< Updated upstream
                embedding_function=embedding_functions.DefaultEmbeddingFunction()
=======
                embedding_function=embedding_functions.DefaultEmbeddingFunction(),
>>>>>>> Stashed changes
            )

    @staticmethod
    def _chromadb():
        import chromadb

        return chromadb

    @staticmethod
    def _embedding_functions():
        from chromadb.utils import embedding_functions

        return embedding_functions

    @staticmethod
    def get_chroma_client():
        """Get a shared chroma client."""
        global _chroma_client
        if _chroma_client is None:
            chromadb = SemanticRepository._chromadb()
            _chroma_client = chromadb.HttpClient(
                host=settings.chroma_settings.host,
                port=settings.chroma_settings.port,
            )
        return _chroma_client

    async def get_similar_chunks(self, user_input: str, num_of_chunks: int) -> list:
        """Retrieve similar chunks from the configured collection."""
        if self.collection is None:
            return []

        result = await asyncio.to_thread(
            self.collection.query,
            query_texts=[user_input],
            n_results=num_of_chunks,
            include=["documents"],
        )
        return result["documents"][0]
