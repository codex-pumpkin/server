from src.core.exceptions.AppError import AppError

class LLMAuthenticationError(AppError):
    def __init__(self):
        self.message = "Failed to authenticate with the LLM API."
        super().__init__(self.message)