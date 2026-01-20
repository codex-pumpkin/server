
from src.persistence.interfaces import ICodeValidator
from src.core.dtos.validation_result import ValidationResult

class CodeValidator(ICodeValidator):
    async def validate_code(self, code:str) -> ValidationResult:
        ...