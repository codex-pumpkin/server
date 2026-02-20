from src.core.exceptions.AppError import AppError

class LLMAPIError(AppError):
    def __init__(self):
        """
        @return None: Initialize exception instance.
        """
        self.message = "An error occurred while communicating with the LLM API."
        super().__init__(self.message)
