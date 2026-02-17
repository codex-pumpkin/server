from src.core.exceptions.AppError import AppError

class LLMNotFoundError(AppError):
    def __init__(self):
        """Initialize the instance."""
        self.message = "The requested LLM resource was not found."
        super().__init__(self.message)