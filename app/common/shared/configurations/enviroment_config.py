from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    
    JWT_VALIDATE_ISSUER: bool = False
    JWT_VALIDATE_AUDIENCE: bool = False
    JWT_VALIDATE_LIFETIME: bool = True
    JWT_VALIDATE_ISSUER_SIGNING_KEY: bool = True
    JWT_VALID_ISSUER: str = "http://localhost:5000"
    JWT_VALID_AUDIENCE: str = "http://localhost:3000"
    JWT_ISSUER_SIGNING_KEY: str = "menudigital231@3123adaw;o412!e21dsawe213sda"
    JWT_CLOCK_SKEW: int = 0
    JWT_EXPIRE_MINUTES: int = 30
    JWT_REFRESH_TOKEN_EXPIRE_MINUTES: int = 1
    
settings = Settings()