from src.core.exceptions.AppError import AppError

class UserConflictError(AppError):
    """Raised when a user field (email/username) already exists"""
    def __init__(self, field: str, message: str = None):
        self.field = field
        self.message = message or f"The {field} is already taken."
        super().__init__(self.message)