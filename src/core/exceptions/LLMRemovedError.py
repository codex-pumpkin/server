from src.core.exceptions.AppError import AppError

class LLMRemovedError(AppError):
    def __init__(self):
        """
        @return None: Initialize exception instance.
        """
        self.message = "The LLM model used in that chat was deleted."
        super().__init__(self.message)
