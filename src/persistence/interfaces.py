from typing import Protocol

class ISemanticRepository(Protocol):
    def get_similar_chunks(user_input, num_of_chunks) -> list:
        ...