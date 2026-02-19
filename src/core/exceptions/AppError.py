class AppError(Exception):
    """Base class for all application-specific errors"""
    def __init__(self, message: str):
        """
        @param message (str): Human-readable error message.
        @return None: Initialize exception instance.
        """
        self.message = message
        super().__init__(self.message)

