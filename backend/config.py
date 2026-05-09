"""Configuration module.

Uses Pydantic's BaseSettings to load environment variables from a .env file.
"""

from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    # Application metadata
    APP_NAME: str = Field("Medical Diagnostic API", env="APP_NAME")
    APP_DESCRIPTION: str = Field(
        "API for managing patient diagnostics and anomaly detection.", env="APP_DESCRIPTION"
    )
    APP_VERSION: str = Field("0.1.0", env="APP_VERSION")

    # Database configuration
    DATABASE_URL: str = Field(..., env="DATABASE_URL")

    # Encryption key for sensitive fields (base64 encoded 32‑byte key)
    ENCRYPTION_KEY: str = Field(..., env="ENCRYPTION_KEY")

    # JWT configuration
    JWT_SECRET_KEY: str = Field(..., env="JWT_SECRET_KEY")
    JWT_ALGORITHM: str = Field("HS256", env="JWT_ALGORITHM")
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(30, env="JWT_ACCESS_TOKEN_EXPIRE_MINUTES")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Instantiate settings for use in the application
settings = Settings()
