from src.core.exceptions.AppError import AppError

class VerificationError(AppError):
    def __init__(self, message: str = "Verification failed"):
        """Initialize the instance."""
        super().__init__(message)