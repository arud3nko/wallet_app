from pydantic_settings import BaseSettings, SettingsConfigDict


class BotSettings(BaseSettings):
    """Provides database configuration"""

    TOKEN: str

    model_config = SettingsConfigDict(env_file="bot.env")


settings = BotSettings()
