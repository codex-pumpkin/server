from chromadb.utils import embedding_functions


class SemanticRepository():
    def __init__(self, chroma_client):
        self.collection = chroma_client.get_or_create_collection(
            name="SPICE_Docs",
            embedding_function=embedding_functions.DefaultEmbeddingFunction()
        )   

    ''' Retrieve similar text chunks from the collection based on user input
        input: user_input - the input text to find similar chunks for, in embedding form
        num_of_chunks - number of similar chunks to retrieve
        output: list of similar text chunks
    '''
    def get_similar_chunks(self, user_input: list[float], num_of_chunks: int) -> list:
        result = self.collection.query(
            query_embeddings=[user_input],
            n_results=num_of_chunks,
        )
        return result["documents"]