
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Annotated


class MailSettings(BaseModel):
    smtp_server:str
    port:int = Field(ge=0, lt=0xFFFF)
    app_mail:Annotated[str, EmailStr]
    password:str
    logo:str


class Settings(BaseModel):
    mail_settings: MailSettings

mail_settings = MailSettings(
    smtp_server="smtp.gmail.com",
    port=465,
    app_mail="codex.mail.kit@gmail.com",
    password="qmgp zach rxny otbs",
    logo="https://avatars.githubusercontent.com/u/246187360?s=400&u=5ffccaf72b3fb7f855e275fabf1ab438fded4a0a&v=4"
)

settings = Settings(
    mail_settings=mail_settings
)