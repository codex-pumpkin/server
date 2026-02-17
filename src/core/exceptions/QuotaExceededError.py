from src.core.exceptions.AppError import AppError
from typing import Optional

class QuotaExceededError(AppError):
    def __init__(self, message: Optional[str] = None):
        """Initialize the instance."""
        self.message = message or "You have exceeded your daily quota!"
        super().__init__(self.message)