from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BASE_DIR: Path = Path(__file__).parent.parent.resolve()

    SECRET_KEY: str
    DEBUG: bool = True

    POSTGRES_DB: str = "db"
    POSTGRES_USER: str = "db"
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: int = 5432

    CELERY_BROKER_URL: str = "redis://redis:6379/0"

    TELEGRAM_BOT_TOKEN: str
    API_BASE_URL: str = "http://api:8000/api/v1"

    @property
    def db_url(self) -> str:
        return f"postgres://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(
        env_file=f"{BASE_DIR}/.env",
        env_file_encoding="utf-8",
    )


settings = Settings()
