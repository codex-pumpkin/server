
from typing import Protocol
from typing_extensions import runtime_checkable
from abc import ABC, abstractmethod

@runtime_checkable
class IGraphGenerator(ABC):
    @abstractmethod
    async def gen_graph(self, code:str) -> bool:
        ...