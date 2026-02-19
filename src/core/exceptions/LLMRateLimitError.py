from src.core.exceptions.AppError import AppError

class LLMRateLimitError(AppError):
    def __init__(self):
        """
        @return None: Initialize exception instance.
        """
        self.message = "The LLM API rate limit has been exceeded."
        super().__init__(self.message)
