
from typing import Protocol
from typing_extensions import runtime_checkable
from abc import abstractmethod, ABC

class ICodeValidator(ABC):
    @abstractmethod
    async def validate_code(self, code:str) -> bool:
        ...