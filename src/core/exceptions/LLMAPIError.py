from src.core.exceptions.AppError import AppError

class LLMAPIError(AppError):
    def __init__(self):
        """Initialize the instance."""
        self.message = "An error occurred while communicating with the LLM API."
        super().__init__(self.message)