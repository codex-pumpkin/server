from src.core.exceptions.AppError import AppError

class LLMBadRequestError(AppError):
    def __init__(self):
        """Initialize the instance."""
        self.message = "The LLM API received a bad request."
        super().__init__(self.message)