from pathlib import Path
import chromadb
from chromadb.utils import embedding_functions
from typing import Optional, Union

_chroma_client: Optional[chromadb.PersistentClient] | None = None

class SemanticRepository():
    
    def __init__(self, namedb: str="SPICE_Docs") -> None:
        self.collection = self.get_chroma_client().get_collection(
            name=namedb,
            embedding_function=embedding_functions.DefaultEmbeddingFunction()
        )   
    
    """ Get a singleton ChromaDB client instance """
    @staticmethod
    def get_chroma_client(source:Union[Path, str]="./chroma_database/chroma_db") -> chromadb.PersistentClient:
        global _chroma_client
        if _chroma_client is None:
            _chroma_client = chromadb.PersistentClient(path=source)
        return _chroma_client

    ''' Retrieve similar text chunks from the collection based on user input
        input: user_input - the input text to find similar chunks for, in embedding form
        num_of_chunks - number of similar chunks to retrieve
        output: list of similar text chunks
    '''
    def get_similar_chunks(self, user_input: str, num_of_chunks: int) -> list:
        result = self.collection.query(
            query_texts=[user_input],
            n_results=num_of_chunks,
            include=["documents"]
        )
        return result["documents"][0]