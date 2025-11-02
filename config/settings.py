from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TELEGRAM_TOKEN: str
    TELEGRAM_CHAT_ID: str
    RWBY_URL: str
    RWBY_TIMEOUT: int

    class Config:
        env_file = ".env"


settings = Settings()
