from src.core.exceptions.AppError import AppError

class LLMAPIConnectionError(AppError):
    def __init__(self):
        """
        @return None: Initialize exception instance.
        """
        self.message = "Failed to connect to the LLM API."
        super().__init__(self.message)
