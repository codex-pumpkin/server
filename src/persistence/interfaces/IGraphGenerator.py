
from typing import Protocol
from typing_extensions import runtime_checkable
from abc import ABC, abstractmethod

class IGraphGenerator(ABC):
    @abstractmethod
    async def gen_graph(self, code:str) -> str:
        """Gen graph."""
        ...
