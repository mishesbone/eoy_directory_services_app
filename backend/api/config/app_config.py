import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "eOY Directory Services"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
