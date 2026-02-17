from src.core.exceptions.AppError import AppError

class AuthError(AppError):
    def __init__(self, message: str = "Authentication failed"):
        """Initialize the instance."""
        super().__init__(message)