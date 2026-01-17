
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Annotated


class MailSettings(BaseModel):
    smtp_server:str
    port:int = Field(ge=0, lt=0xFFFF)
    app_mail:Annotated[str, EmailStr]
    password:str
    logo:str

class JWTSettings(BaseModel):
    algorithm:str
    secret_key:str
    expire_time:int

class RefreshSettings(BaseModel):
    expire_time:int

class Settings(BaseModel):
    mail_settings: MailSettings
    jwt_settings: JWTSettings
    refresh_settings: RefreshSettings

mail_settings = MailSettings(
    smtp_server="smtp.gmail.com",
    port=465,
    app_mail="codex.mail.kit@gmail.com",
    password="qmgp zach rxny otbs",
    logo="https://avatars.githubusercontent.com/u/246187360?s=400&u=5ffccaf72b3fb7f855e275fabf1ab438fded4a0a&v=4"
)

jwt_settings = JWTSettings(
    algorithm="HS256",
    secret_key="secret",
    expire_time=15
)

refresh_settings = RefreshSettings(
    expire_time= 1 * 30 * 24 * 60
)

settings = Settings(
    mail_settings=mail_settings,
    jwt_settings=jwt_settings,
    refresh_settings=refresh_settings
)
