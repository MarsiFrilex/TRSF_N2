from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')


class Config(Settings):
    DB_URL: str = ""


config = Config()