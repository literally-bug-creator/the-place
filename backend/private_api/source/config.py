from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    path: str = Field(validation_alias="APP_PATH")
    host: str = Field(validation_alias="APP_HOST")
    port: int = Field(validation_alias="APP_PORT")
    should_reload: bool = Field(validation_alias="APP_SHOULD_RELOAD")


def get_app_settings() -> AppSettings:
    return AppSettings()  # type: ignore
