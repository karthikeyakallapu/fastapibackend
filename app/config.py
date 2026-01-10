from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=False)

    app_name:str
    version :str
    debug : bool
    environment: str

    # Server
    host: str = "127.0.0.1"
    port: int = 5174

    # Logging
    log_level: str = "INFO"

    @field_validator("app_name", "version", "environment")
    @classmethod
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("must not be empty")
        return v


settings = Settings()

