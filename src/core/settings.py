
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Annotated
from dotenv import load_dotenv
import os


def getenv(name: str, default: str) -> str:
    value = os.getenv(name)
    return value if value is not None else default

class MailSettings(BaseModel):
    """
    Mail transport and branding configuration.

    @param smtp_server (str): SMTP host used to send transactional emails.
    @param port (int): SMTP port number.
    @param app_mail (Annotated[str, EmailStr]): Sender email address.
    @param password (str): App password or SMTP credential.
    @param logo (str): Public logo URL used in email templates.
    @param client_base_url (str): Client application base URL for email links.
    """
    """
    Mail transport and branding configuration.

    @param smtp_server (str): SMTP host used to send transactional emails.
    @param port (int): SMTP port number.
    @param app_mail (Annotated[str, EmailStr]): Sender email address.
    @param password (str): App password or SMTP credential.
    @param logo (str): Public logo URL used in email templates.
    @param client_base_url (str): Client application base URL for email links.
    """
    smtp_server:str
    port:int = Field(ge=0, lt=0xFFFF)
    app_mail:Annotated[str, EmailStr]
    password:str
    logo:str
    client_base_url:str
    client_base_url:str
    verification_required:bool

class JWTSettings(BaseModel):
    """
    JWT token configuration.

    @param algorithm (str): JWT signing algorithm.
    @param secret_key (str): Secret key used for JWT signing and validation.
    @param expire_time (int): Access-token expiry time in minutes.
    """
    """
    JWT token configuration.

    @param algorithm (str): JWT signing algorithm.
    @param secret_key (str): Secret key used for JWT signing and validation.
    @param expire_time (int): Access-token expiry time in minutes.
    """
    algorithm:str
    secret_key:str
    expire_time:int

class RefreshSettings(BaseModel):
    """
    Refresh-token configuration.

    @param expire_time (int): Refresh-token expiry time in minutes.
    """
    """
    Refresh-token configuration.

    @param expire_time (int): Refresh-token expiry time in minutes.
    """
    expire_time:int    

class LLMSettings(BaseModel):
    """
    LLM generation behavior configuration.

    @param num_of_regenerations (int): Maximum regeneration attempts after validation failure.
    """
    """
    LLM generation behavior configuration.

    @param num_of_regenerations (int): Maximum regeneration attempts after validation failure.
    """
    api_key:str
    num_of_regenerations: int

class GoogleAuthSettings(BaseModel):
    """
    Google OAuth client configuration.

    @param client_id (str): OAuth client identifier.
    @param redirect_uri (str): OAuth callback URI used by this server.
    @param url (str): Google OAuth authorization endpoint base URL.
    @param client_secret (str): OAuth client secret.
    @param token_url (str): Google OAuth token exchange endpoint.
    @param user_info_url (str): Google user-info endpoint URL.
    """
    """
    Google OAuth client configuration.

    @param client_id (str): OAuth client identifier.
    @param redirect_uri (str): OAuth callback URI used by this server.
    @param url (str): Google OAuth authorization endpoint base URL.
    @param client_secret (str): OAuth client secret.
    @param token_url (str): Google OAuth token exchange endpoint.
    @param user_info_url (str): Google user-info endpoint URL.
    """
    client_id: str
    redirect_uri: str
    url: str
    client_secret: str
    token_url: str
    user_info_url: str
    
class DatabaseSettings(BaseModel):
    url: str

class ChromaSettings(BaseModel):
    host: str
    port: int
    chunk_size: int
    chunk_overlap: int
    num_of_chunks: int
    
class PicturesSettings(BaseModel):
    """
    Pictures storage configuration.

    @param path (str): Path to the directory where profile pictures are stored.
    """
    path: str

class AdminSettings(BaseModel):
    email: str
    username: str
    password: str

class Settings(BaseModel):
    """
    Aggregated application settings container.

    @param mail_settings (MailSettings): Email transport settings.
    @param jwt_settings (JWTSettings): JWT settings.
    @param refresh_settings (RefreshSettings): Refresh-token settings.
    @param llm_settings (LLMSettings): LLM runtime settings.
    @param google_settings (GoogleAuthSettings): Google OAuth settings.
    @param database_settings (DatabaseSettings): Database connection settings.
    """
    mail_settings: MailSettings
    jwt_settings: JWTSettings
    refresh_settings: RefreshSettings
    llm_settings: LLMSettings
    google_settings: GoogleAuthSettings
    database_settings: DatabaseSettings
    pictures_settings: PicturesSettings
    chroma_settings: ChromaSettings
    admin_settings: AdminSettings
    

load_dotenv()

mail_settings = MailSettings(
    smtp_server=os.getenv("APP_MAIL_SMTP_SERVER", "smtp.example.com"),
    port=os.getenv("APP_MAIL_SMTP_PORT", "465"),
    app_mail=os.getenv("APP_MAIL", "mail@example.com"),
    password=os.getenv("MAIL_PASSWORD", "password"),
    logo="https://avatars.githubusercontent.com/u/246187360?s=400&u=5ffccaf72b3fb7f855e275fabf1ab438fded4a0a&v=4",
    client_base_url=os.getenv("CLIENT_BASE_URL", ""),
    verification_required=not (os.getenv("EMAIL_VERIFICATION_REQUIRED", "true").lower() == "false")
)

jwt_settings = JWTSettings(
    algorithm="HS256",
    secret_key=os.getenv("JWT_SECRET", ""),
    expire_time=15
)

refresh_settings = RefreshSettings(
    expire_time= 1 * 30 * 24 * 60
)

llm_settings = LLMSettings(
    api_key=os.getenv("OPENAI_API_KEY", ""),
    num_of_regenerations=1,
)

google_settings = GoogleAuthSettings(
    client_id=os.getenv("CLIENT_ID", ""),
    token_url="https://oauth2.googleapis.com/token",
    client_secret=os.getenv("CLIENT_SECRET", ""),
    redirect_uri="http://localhost:8000/auth/google/callback",
    url="https://accounts.google.com/o/oauth2/auth?",
    user_info_url="https://www.googleapis.com/oauth2/v3/userinfo"
)

database_settings = DatabaseSettings(
    url=getenv("DATABASE_URL", "sqlite+aiosqlite:///:memory:")
)

pictures_settings = PicturesSettings(
    path="/app/pictures"
)

chroma_settings = ChromaSettings(
    host=getenv("CHROMA_HOST", "localhost"),
    port=getenv("CHROMA_PORT", "8000"),
    chunk_size= 500,
    chunk_overlap= 100,
    num_of_chunks= 2,
)

admin_settings = AdminSettings(
    email=getenv("ADMIN_EMAIL", "admin@example.com"),
    username=getenv("ADMIN_USERNAME", "admin"),
    password=getenv("ADMIN_PASSWORD", "admin")
)

settings = Settings(
    mail_settings=mail_settings,
    jwt_settings=jwt_settings,
    refresh_settings=refresh_settings,
    llm_settings=llm_settings,
    google_settings=google_settings,
    database_settings=database_settings,
    pictures_settings=pictures_settings,
    chroma_settings=chroma_settings,
    admin_settings=admin_settings
)
