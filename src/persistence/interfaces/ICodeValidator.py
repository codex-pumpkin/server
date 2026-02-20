
from typing import Protocol
from typing_extensions import runtime_checkable
from abc import abstractmethod, ABC
from src.core.dtos.validation_result import ValidationResult

class ICodeValidator(ABC):
    @abstractmethod
    async def validate_code(self, code:str) -> ValidationResult:
        """Validate code."""
        ...
