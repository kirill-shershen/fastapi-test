import os
from functools import lru_cache

from pydantic import BaseSettings


SETTINGS_FILE = os.getenv("ENV_FILE", ".env")


class Settings(BaseSettings):
    debug: bool = False
    app_name: str = "Rialto"
    admin_email: str = ""
    access_token_expire_minutes: int = 60
    algorithm: str = "HS256"
    secret_key: str = "11d197649061838c0c381612cb44462ff181f2ed68c7847471af22f83ce2aa2"
    db_name: str = "postgres"
    db_password: str = "postgres"
    db_user: str = "postgres"
    db_host: str = "postgres"
    db_port: str = "5432"
    database_url: str = f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    class Config:
        env_file = SETTINGS_FILE


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
