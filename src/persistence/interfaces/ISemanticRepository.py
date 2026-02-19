from typing import Protocol, List
from typing_extensions import runtime_checkable
from abc import ABC, abstractmethod

class ISemanticRepository(ABC):
    @abstractmethod
    def get_similar_chunks(self, user_input, num_of_chunks) -> List:
        """Get similar chunks."""
        ...
