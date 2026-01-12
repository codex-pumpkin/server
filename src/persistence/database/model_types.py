
import uuid
from typing import Annotated
from sqlalchemy import String, func
from sqlalchemy.orm import mapped_column
import datetime

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
