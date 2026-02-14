
from src.core.exceptions.AppError import AppError
from typing import Optional

class UserConflictError(AppError):
    """Raised when a user field (email/username) already exists"""
    def __init__(self, field: str, message: Optional[str] = None):
        self.field = field
        self.message = message or f"The {field} is already taken."
        super().__init__(self.message)