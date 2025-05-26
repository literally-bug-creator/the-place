from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    path: str = Field(validation_alias="APP_PATH")
    host: str = Field(validation_alias="APP_HOST")
    port: int = Field(validation_alias="APP_PORT")
    should_reload: bool = Field(validation_alias="APP_SHOULD_RELOAD")


class AuthSettings(BaseSettings):
    algorithm: str = Field(default="RS256", validation_alias="JWT_ALGORITHM")
    private_key_path: str = Field(validation_alias="JWT_PRIVATE_KEY_PATH")
    public_key_path: str = Field(validation_alias="JWT_PUBLIC_KEY_PATH")
    token_lifetime: int = Field(validation_alias="JWT_TOKEN_LIFETIME")
    token_type: str = Field(default="Bearer", validation_alias="JWT_TOKEN_TYPE")


def get_app_settings() -> AppSettings:
    return AppSettings()  # type: ignore


def get_auth_settings() -> AuthSettings:
    return AuthSettings()  # type: ignore
