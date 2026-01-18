
from src.persistence.interfaces import ICodeValidator

class CodeValidator(ICodeValidator):
    async def validate_code(self, code:str) -> bool:
        ...