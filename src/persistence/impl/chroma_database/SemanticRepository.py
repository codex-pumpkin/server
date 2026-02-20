import asyncio
import asyncio
from pathlib import Path
from unittest import result
from unittest import result
import chromadb
from chromadb.utils import embedding_functions
from typing import Optional, Union
from src.persistence.interfaces import ISemanticRepository

_chroma_client: Optional[chromadb.PersistentClient] | None = None

class SemanticRepository(ISemanticRepository):

    def __init__(self, namedb: str="SPICE_Docs") -> None:
        """Initialize the instance."""
        self.collection = self.get_chroma_client().get_collection(
            name=namedb,
            embedding_function=embedding_functions.DefaultEmbeddingFunction()
        )

    @staticmethod
    def get_chroma_client() -> chromadb.PersistentClient:
        """Get chroma client."""
        global _chroma_client
        if _chroma_client is None:
            _chroma_client = chromadb.HttpClient(host="chroma", port=8000)
        return _chroma_client


    async def get_similar_chunks(self, user_input: str, num_of_chunks: int) -> list:
        """ 
        Retrieve similar text chunks from the collection based on user input
        input: user_input - the input text to find similar chunks for, in embedding form
        num_of_chunks - number of similar chunks to retrieve
        output: list of similar text chunks
        """
        result = await asyncio.to_thread(
            self.collection.query,
            query_texts=[user_input],
            n_results=num_of_chunks,
            include=["documents"]
        )
        return result["documents"][0]
    
