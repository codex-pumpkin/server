from src.core.exceptions.AppError import AppError

class LLMAuthenticationError(AppError):
    def __init__(self):
        """Initialize the instance."""
        self.message = "Failed to authenticate with the LLM API."
        super().__init__(self.message)