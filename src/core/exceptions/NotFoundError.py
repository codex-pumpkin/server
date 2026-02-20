
from src.core.exceptions.AppError import AppError

class NotFoundError(AppError):
    def __init__(self, type_of: str, id_of:str):
        """
        @param type_of (str): Resource type that was not found.
        @param id_of (str): Missing resource identifier.
        @return None: Initialize exception instance.
        """
        self.message = f"{type_of} with id: {id_of} is not found!"
        super().__init__(self.message)
