
import uuid
from typing import Annotated
from sqlalchemy import String, func
from sqlalchemy.orm import mapped_column
import datetime
import random

uuid_pk = Annotated[
        str,
        mapped_column(
            String(36),
            primary_key=True,
            default=lambda: str(uuid.uuid4())
        )
]

created_at_type = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=func.now()
    )
]



def generate_code() -> str:
    out = ""
    for _ in range(6):
        out += random.randint(0, 9)
    return out

verification_code = Annotated[
    str,
    mapped_column(default=lambda: generate_code())
]