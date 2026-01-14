from typing import Protocol, List
from typing_extensions import runtime_checkable

@runtime_checkable
class ISemanticRepository(Protocol):
    def get_similar_chunks(user_input, num_of_chunks) -> list:
        ...