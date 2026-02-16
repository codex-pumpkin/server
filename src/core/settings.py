
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Annotated
from dotenv import load_dotenv
import os

class MailSettings(BaseModel):
    smtp_server:str
    port:int = Field(ge=0, lt=0xFFFF)
    app_mail:Annotated[str, EmailStr]
    password:str
    logo:str
    client_base_url:str

class JWTSettings(BaseModel):
    algorithm:str
    secret_key:str
    expire_time:int

class RefreshSettings(BaseModel):
    expire_time:int

class LLMSettings(BaseModel):
    num_of_regenerations: int

class GoogleAuthSettings(BaseModel):
    client_id: str
    redirect_uri: str
    url: str
    client_secret: str
    token_url: str
    user_info_url: str

class Settings(BaseModel):
    mail_settings: MailSettings
    jwt_settings: JWTSettings
    refresh_settings: RefreshSettings
    llm_settings: LLMSettings
    google_settings: GoogleAuthSettings

load_dotenv()

mail_settings = MailSettings(
    smtp_server=os.getenv("APP_MAIL_SMTP_SERVER"),
    port=os.getenv("APP_MAIL_SMTP_PORT"),
    app_mail=os.getenv("APP_MAIL"),
    password=os.getenv("MAIL_PASSWORD"),
    logo="https://avatars.githubusercontent.com/u/246187360?s=400&u=5ffccaf72b3fb7f855e275fabf1ab438fded4a0a&v=4",
    client_base_url=os.getenv("CLIENT_BASE_URL")
)

jwt_settings = JWTSettings(
    algorithm="HS256",
    secret_key=os.getenv("JWT_SECRET"),
    expire_time=15
)

refresh_settings = RefreshSettings(
    expire_time= 1 * 30 * 24 * 60
)

llm_settings = LLMSettings(
    num_of_regenerations=1,
)

google_settings = GoogleAuthSettings(
    client_id=os.getenv("CLIENT_ID"),
    token_url="https://oauth2.googleapis.com/token",
    client_secret=os.getenv("CLIENT_SECRET"),
    redirect_uri="http://localhost:8000/auth/google/callback",
    url="https://accounts.google.com/o/oauth2/auth?",
    user_info_url="https://www.googleapis.com/oauth2/v3/userinfo"
)

settings = Settings(
    mail_settings=mail_settings,
    jwt_settings=jwt_settings,
    refresh_settings=refresh_settings,
    llm_settings=llm_settings,
    google_settings=google_settings
)
