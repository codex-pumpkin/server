from src.core.exceptions.AppError import AppError

class LLMPermissionDeniedError(AppError):
    def __init__(self):
        """Initialize the instance."""
        self.message = "The LLM API denied permission to access the requested resource."
        super().__init__(self.message)