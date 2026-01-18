from pydantic import BaseModel

class ValidationResult(BaseModel):
    isValid: bool
    exitCode: int
    rawOutput: str