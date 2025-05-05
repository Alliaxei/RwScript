from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    TELEGRAM_TOKEN: str
    TELEGRAM_CHAT_ID: str

    RWBY_URL: str = "https://pass.rw.by/ru/route/?from=%D0%92%D0%B8%D1%82%D0%B5%D0%B1%D1%81%D0%BA&from_exp=&from_esr=&to=%D1%80%D0%BE%D0%B3%D0%B0%D1%87%D0%B5%D0%B2&to_exp=&to_esr=&front_date=8+%D0%BC%D0%B0%D1%8F.+2025&date=2025-05-08"
    RWBY_TIMEOUT: int = 100000

    class Config:
        env_file = ".env"

settings = Settings()