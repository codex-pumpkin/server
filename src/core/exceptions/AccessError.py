
from src.core.exceptions.AppError import AppError

class AccessError(AppError):
    def __init__(self, type_of: str, id_of:str):
        """Initialize the instance."""
        self.message = f"You dont have access to {type_of} with id: {id_of}"
        super().__init__(self.message)