from src.core.exceptions.AppError import AppError

class AuthError(AppError):
    def __init__(self, message: str = "Authentication failed"):
        """
        @param message (str): Authentication failure message.
        @return None: Initialize exception instance.
        """
        super().__init__(message)
