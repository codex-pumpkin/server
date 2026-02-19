from src.core.exceptions.AppError import AppError

class VerificationError(AppError):
    def __init__(self, message: str = "Verification failed"):
        """
        @param message (str): Verification failure message.
        @return None: Initialize exception instance.
        """
        super().__init__(message)
