from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    
    JWT_VALIDATE_ISSUER: bool = os.getenv("JWT_VALIDATE_ISSUER")
    JWT_VALIDATE_AUDIENCE: bool = os.getenv("JWT_VALIDATE_AUDIENCE")
    JWT_VALIDATE_LIFETIME: bool = os.getenv("JWT_VALIDATE_LIFETIME")
    JWT_VALIDATE_ISSUER_SIGNING_KEY: bool = os.getenv("JWT_VALIDATE_ISSUER_SIGNING_KEY")
    JWT_VALID_ISSUER: str = os.getenv("JWT_VALID_ISSUER")
    JWT_VALID_AUDIENCE: str = os.getenv("JWT_VALID_AUDIENCE")
    JWT_ISSUER_SIGNING_KEY: str = os.getenv("JWT_ISSUER_SIGNING_KEY")
    JWT_EXPIRE_MINUTES: int = os.getenv("JWT_EXPIRE_MINUTES")
    JWT_REFRESH_TOKEN_EXPIRE_MINUTES: int = os.getenv("JWT_REFRESH_TOKEN_EXPIRE_MINUTES")
    
    MAIL_USERNAME: str = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD: str= os.getenv("MAIL_PASSWORD")
    MAIL_FROM:str = os.getenv("MAIL_FROM")
    MAIL_PORT:int = os.getenv("MAIL_PORT")
    MAIL_SERVER: str = os.getenv("MAIL_SERVER")
    MAIL_TLS: bool = os.getenv("MAIL_TLS")
    MAIL_SSL: bool = os.getenv("MAIL_SSL")
    USE_CREDENTIALS: bool = os.getenv("USE_CREDENTIALS")
    
settings = Settings()